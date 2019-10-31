// set the dimensions and margins of the graph
var width = 1000
var height = 1000

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
  .append("svg")
  .attr("width", width)
  .attr("height", height)
  .append("g")
  .attr("transform", "translate(30,0)");  // bit of margin on the left = 40

// read json data
//d3.json("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/data_dendrogram.json", function(data) {

d3.json("static/data/housecrimes2018.json", function (data) {

  //console.log("test " + data.children[0].color)

  // Create the cluster layout:
  var cluster = d3.cluster()
    .size([height, width - 250]);  // 100 is the margin I will have on the right side

  nodeValues = ["NYC"]

  // Give the data to this cluster layout:
  var root = d3.hierarchy(data, function (d, i) {
    return d.children;
  });
  cluster(root);




  for (var i = 0; i < 5; i++) {
    //console.log(data.children[i].name)
    nodeValues.push(data.children[i].name)

  }

  for (var i = 0; i < 5; i++) {
    for (var j = 0; j < 3; j++) {
      //console.log(data.children[i].children[j].name)
      nodeValues.push(data.children[i].children[j].name)
    }

  }

  for (var i = 0; i < 5; i++) {
    for (var j = 0; j < 3; j++) {
      for (var k = 0; k < 3; k++) {
        //console.log(data.children[i].children[j].children[k].name)
        nodeValues.push(data.children[i].children[j].children[k].name)
      }
    }
  }

  console.log(nodeValues)



  // Add the links between nodes:
  svg.selectAll('path')
    .data(root.descendants().slice(1))
    .enter()
    .append('path')
    .attr("d", function (d) {
      return "M" + d.y + "," + d.x
        + "C" + (d.parent.y + 50) + "," + d.x
        + " " + (d.parent.y + 150) + "," + d.parent.x // 50 and 150 are coordinates of inflexion, play with it to change links shape
        + " " + d.parent.y + "," + d.parent.x;
    })
    .style("fill", 'none')
    .attr("stroke", '#ccc')


  // // Add a circle for each node.
  // svg.selectAll("g")
  //     .data(root.descendants())
  //     .enter()
  //     .append("g")
  //     .attr("transform", function(d) {
  //         return "translate(" + d.y + "," + d.x + ")"
  //     })
  //     .append("circle")
  //       .attr("r", 7)
  //       .style("fill", "#69b3a2")
  //       .attr("stroke", "black")
  //       .style("stroke-width", 2)  

  var node = svg.selectAll("g")
    .data(root.descendants())
    .enter()
    .append("g")
    .attr("transform", function (d) {
      return "translate(" + d.y + "," + d.x + ")"
    })

  var colors = ["magenta",
    "red",
    "steelblue",
    "goldenrod",
    "forestgreen",
    "mediumturquoise",
    "red",
    "red",
    "red",
    "steelblue",
    "steelblue",
    "steelblue",
    "goldenrod",
    "goldenrod",
    "goldenrod",
    "forestgreen",
    "forestgreen",
    "forestgreen",
    "mediumturquoise",
    "mediumturquoise",
    "mediumturquoise",
    "red",
    "red",
    "red",
    "red",
    "red",
    "red",
    "red",
    "red",
    "red",
    "steelblue",
    "steelblue",
    "steelblue",
    "steelblue",
    "steelblue",
    "steelblue",
    "steelblue",
    "steelblue",
    "steelblue",
    "goldenrod",
    "goldenrod",
    "goldenrod",
    "goldenrod",
    "goldenrod",
    "goldenrod",
    "goldenrod",
    "goldenrod",
    "goldenrod",
    "forestgreen",
    "forestgreen",
    "forestgreen",
    "forestgreen",
    "forestgreen",
    "forestgreen",
    "forestgreen",
    "forestgreen",
    "forestgreen",
    "mediumturquoise",
    "mediumturquoise",
    "mediumturquoise",
    "mediumturquoise",
    "mediumturquoise",
    "mediumturquoise",
    "mediumturquoise",
    "mediumturquoise",
    "mediumturquoise",
  ]






  node.append("circle")
    .attr("r", 7)
    .style("fill", function (d, i) { return colors[i] })
    .attr("stroke", "black")
    .style("stroke-width", 2)

  node.append("text")
    .attr("dx", 15)
    .attr("dy", 15)
    .text(function (d, i) { return nodeValues[i] })




  // node.simulation
  //   .on("tick", ticked);







})



