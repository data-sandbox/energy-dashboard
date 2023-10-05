import altair as alt

plotWidth = 500
plotHeight = 350
highlight = alt.selection_point(
    on='mouseover', fields=['seriesDescription'], nearest=True)


def mark_chart(base):
    """Add lines and highlight interactivity"""
    points = base.mark_circle().encode(
        opacity=alt.value(0)
    ).add_params(
        highlight
    ).properties(
        width=plotWidth,
        height=plotHeight
    )

    lines = base.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )
    return points + lines


def plot_overview_monthly(df):
    base = alt.Chart(df).encode(
        x=alt.X('period:T', axis=alt.Axis(
            format="%Y %m", tickCount="month"), title='Month'),
        y=alt.Y('value:Q', title='Energy Consumption (Trillion Btu)'),
        color=alt.Color('seriesDescription:N', legend=None),
        tooltip='seriesDescription:N',
    )
    return mark_chart(base)


def plot_overview_annual(df):
    base = alt.Chart(df).encode(
        x=alt.X('period:T', title='Year'),
        y=alt.Y('value:Q', title='Energy Consumption (Trillion Btu)'),
        color=alt.Color('seriesDescription:N', legend=None),
        tooltip='seriesDescription:N',
    )
    return mark_chart(base)


def plot_prices_monthly(df):
    base = alt.Chart(df).encode(
        x=alt.X('period:T', axis=alt.Axis(
            format="%Y %m", tickCount="month"), title='Month'),
        y=alt.Y('value:Q', title='Cents per kWh (taxes included)'),
        color=alt.Color('seriesDescription:N', legend=None),
        tooltip='seriesDescription:N',
    )
    return mark_chart(base)


def plot_prices_annual(df):
    base = alt.Chart(df).encode(
        x=alt.X('period:T', title='Year'),
        y=alt.Y('value:Q', title='Cents per kWh (taxes included)'),
        color=alt.Color('seriesDescription:N', legend=None),
        tooltip='seriesDescription:N',
    )
    return mark_chart(base)


def plot_monthly(df, title):
    base = alt.Chart(df).encode(
        x=alt.X('period:T', axis=alt.Axis(
            format="%Y %m", tickCount="month"), title='Month'),
        y=alt.Y('value:Q', title=title),
        color=alt.Color('seriesDescription:N', legend=None),
        tooltip='seriesDescription:N',
    )
    return mark_chart(base)


def plot_annual(df, title):
    base = alt.Chart(df).encode(
        x=alt.X('period:T', title='Year'),
        y=alt.Y('value:Q', title=title),
        color=alt.Color('seriesDescription:N', legend=None),
        tooltip='seriesDescription:N',
    )
    return mark_chart(base)
