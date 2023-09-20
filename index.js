// Data
d3.csv(
  "MER_T01_03.csv",
  // Label rows as either annual or monthly figures
  function (d) {
    function getPeriod(string) {
      const month = string.slice(4, 6);
      if (month == "13") {
        return "annual";
      } else {
        return "monthly";
      }
    }
    // Format data
    return {
      date: d3.timeParse("%Y%m")(d.YYYYMM),
      period: getPeriod(d.YYYYMM),
      value: +d.Value,
      description: d.Description,
    };
  }
).then(function (rawData) {
  // Filter based on time period
  const data = rawData.filter((d) => d.period === "annual");

  // Specify the chart’s dimensions.
  const width = 928;
  const height = 600;
  const marginTop = 20;
  const marginRight = 20;
  const marginBottom = 30;
  const marginLeft = 30;

  // Create the positional scales.
  const x = d3
    .scaleUtc()
    .domain(d3.extent(data, (d) => d.date))
    .range([marginLeft, width - marginRight]);

  const y = d3
    .scaleLinear()
    .domain([0, d3.max(data, (d) => d.value)])
    .nice()
    .range([height - marginBottom, marginTop]);

  // Create the SVG container.
  const svg = d3
    // .create("svg")
    .select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", [0, 0, width, height])
    .attr(
      "style",
      "max-width: 100%; height: auto; overflow: visible; font: 10px sans-serif;"
    );

  // Add the horizontal axis.
  svg
    .append("g")
    .attr("transform", `translate(0,${height - marginBottom})`)
    .call(
      d3
        .axisBottom(x)
        .ticks(width / 80)
        .tickSizeOuter(0)
    );

  // Add the vertical axis.
  svg
    .append("g")
    .attr("transform", `translate(${marginLeft},0)`)
    .call(d3.axisLeft(y))
    .call((g) => g.select(".domain").remove())
    .call((g) =>
      g
        .append("text")
        .attr("x", -marginLeft)
        .attr("y", 10)
        .attr("fill", "currentColor")
        .attr("text-anchor", "start")
        .text("Energy Consumption (Quadrillion Btu)")
    );

  // Compute the points in pixel space as [x, y, z], where z is the name of the series.
  const points = data.map((d) => [x(d.date), y(d.value), d.description]);

  // Group the points by series.
  const groups = d3.rollup(
    points,
    (v) => Object.assign(v, { z: v[0][2] }),
    (d) => d[2]
  );

  // Draw the lines.
  const line = d3.line();
  const path = svg
    .append("g")
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 1.5)
    .attr("stroke-linejoin", "round")
    .attr("stroke-linecap", "round")
    .selectAll("path")
    .data(groups.values())
    .join("path")
    .style("mix-blend-mode", "multiply")
    .attr("d", line);

  // Add an invisible layer for the interactive tip.
  const dot = svg.append("g").attr("display", "none");

  dot.append("circle").attr("r", 2.5);

  dot.append("text").attr("text-anchor", "middle").attr("y", -8);

  svg
    .on("pointerenter", pointerentered)
    .on("pointermove", pointermoved)
    .on("pointerleave", pointerleft)
    .on("touchstart", (event) => event.preventDefault());

  return svg.node();

  // When the pointer moves, find the closest point, update the interactive tip, and highlight
  // the corresponding line. Note: we don't actually use Voronoi here, since an exhaustive search
  // is fast enough.
  function pointermoved(event) {
    const [xm, ym] = d3.pointer(event);
    const i = d3.leastIndex(points, ([x, y]) => Math.hypot(x - xm, y - ym));
    const [x, y, k] = points[i];
    path
      .style("stroke", ({ z }) => (z === k ? null : "#ddd"))
      .filter(({ z }) => z === k)
      .raise();
    dot.attr("transform", `translate(${x},${y})`);
    dot.select("text").text(k);
    svg.property("value", data[i]).dispatch("input", { bubbles: true });
  }

  function pointerentered() {
    path.style("mix-blend-mode", null).style("stroke", "#ddd");
    dot.attr("display", null);
  }

  function pointerleft() {
    path.style("mix-blend-mode", "multiply").style("stroke", null);
    dot.attr("display", "none");
    svg.node().value = null;
    svg.dispatch("input", { bubbles: true });
  }
});
