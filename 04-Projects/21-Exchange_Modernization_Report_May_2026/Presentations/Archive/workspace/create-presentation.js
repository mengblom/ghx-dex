const pptxgen = require('pptxgenjs');
const html2pptx = require('/Users/mengblom/Documents/ghx-dex/.claude/skills/anthropic-pptx/scripts/html2pptx.js');
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const workspace = '/Users/mengblom/Documents/ghx-dex/04-Projects/Exchange_Modernization_Report_May_2026/Presentations/workspace';

// Create gradient background
async function createGradientBackground() {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="810">
    <defs>
      <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#1C2833"/>
        <stop offset="100%" style="stop-color:#16A085"/>
      </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#g)"/>
  </svg>`;

  await sharp(Buffer.from(svg))
    .png()
    .toFile(path.join(workspace, 'gradient-bg.png'));
}

// Create HTML slides
async function createSlides() {
  // Slide 1: Cover
  fs.writeFileSync(path.join(workspace, 'slide1.html'), `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background-image: url('gradient-bg.png');
  background-size: cover;
  font-family: Arial, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}
.content { text-align: center; color: #ffffff; }
h1 { font-size: 48pt; font-weight: bold; margin: 0 0 20pt 0; }
.subtitle { font-size: 24pt; margin: 0 0 40pt 0; opacity: 0.9; }
.date { font-size: 16pt; opacity: 0.8; }
</style>
</head>
<body>
<div class="content">
  <h1>Exchange Modernization Update</h1>
  <p class="subtitle">Progress, Resiliency & Capacity Outlook</p>
  <p class="date">May 2026</p>
</div>
</body>
</html>`);

  // Slide 2: Agenda
  fs.writeFileSync(path.join(workspace, 'slide2.html'), `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #F8F9FA; font-family: Arial, sans-serif;
  display: flex;
}
.container { margin: 35pt 40pt 50pt 40pt; flex: 1; }
.header-bar { border-left: 8pt solid #16A085; padding-left: 20pt; margin-bottom: 25pt; }
h1 { color: #1C2833; font-size: 36pt; margin: 0; font-weight: bold; }
.item { margin: 0 0 20pt 30pt; }
.number { font-size: 24pt; font-weight: bold; color: #16A085; }
.text { font-size: 18pt; color: #2C3E50; margin: 5pt 0 0 0; }
</style>
</head>
<body>
<div class="container">
  <div class="header-bar">
    <h1>Today's Agenda</h1>
  </div>
  <div class="item">
    <p class="number">1</p>
    <p class="text">Exchange Productivity Commentary - How are things going?</p>
  </div>
  <div class="item">
    <p class="number">2</p>
    <p class="text">Exchange Resiliency - Progress on key initiatives</p>
  </div>
  <div class="item">
    <p class="number">3</p>
    <p class="text">Capacity Forecast - When do we shift to more commercial?</p>
  </div>
</div>
</body>
</html>`);

  // Slide 3: Productivity Assessment
  fs.writeFileSync(path.join(workspace, 'slide3.html'), `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #F8F9FA; font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
}
.header { margin: 30pt 40pt 20pt 40pt; }
.header-bar { border-left: 8pt solid #27AE60; padding-left: 20pt; }
h1 { color: #1C2833; font-size: 32pt; margin: 0; font-weight: bold; }
.content { margin: 0 40pt 40pt 40pt; flex: 1; display: flex; gap: 30pt; }
.left { flex: 1; }
.right { flex: 1; }
.chart-placeholder { width: 100%; height: 240pt; }
</style>
</head>
<body>
<div class="header">
  <div class="header-bar">
    <h1>Productivity: Positive Trends</h1>
  </div>
</div>
<div class="content">
  <div class="left">
    <div id="chart1" class="placeholder chart-placeholder"></div>
  </div>
  <div class="right">
    <div id="chart2" class="placeholder chart-placeholder"></div>
  </div>
</div>
</body>
</html>`);

  // Slide 4: Other Improvements
  fs.writeFileSync(path.join(workspace, 'slide4.html'), `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #F8F9FA; font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
}
.header { margin: 30pt 40pt 20pt 40pt; }
.header-bar { border-left: 8pt solid #16A085; padding-left: 20pt; }
h1 { color: #1C2833; font-size: 32pt; margin: 0; font-weight: bold; }
.content { margin: 0 60pt 50pt 60pt; flex: 1; }
h2 { color: #2C3E50; font-size: 21pt; margin: 20pt 0 10pt 0; font-weight: bold; }
ul { margin: 0; padding-left: 30pt; }
li { font-size: 15pt; color: #34495E; margin: 8pt 0; line-height: 1.3; }
</style>
</head>
<body>
<div class="header">
  <div class="header-bar">
    <h1>Beyond the Metrics: Foundation Building</h1>
  </div>
</div>
<div class="content">
  <h2>Organizational Changes</h2>
  <ul>
    <li>New team topology aligned to future decoupled architecture</li>
    <li>Implementing "Reverse Conway Maneuver" for autonomous teams</li>
  </ul>
  <h2>Talent Upgrade & Hiring</h2>
  <ul>
    <li>Dedicated Engineering Managers and Product Owners for each team</li>
    <li>Key roles being filled to enable independent delivery</li>
    <li>Building GHXi FTE team for Industry Continuity Solution</li>
  </ul>
</div>
</body>
</html>`);

  // Slide 5: Resiliency Table
  fs.writeFileSync(path.join(workspace, 'slide5.html'), `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #F8F9FA; font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
}
.header { margin: 30pt 40pt 20pt 40pt; }
.header-bar { border-left: 8pt solid #16A085; padding-left: 20pt; }
h1 { color: #1C2833; font-size: 32pt; margin: 0; font-weight: bold; }
.content { margin: 0 40pt 40pt 40pt; flex: 1; }
.table-placeholder { width: 100%; height: 260pt; }
</style>
</head>
<body>
<div class="header">
  <div class="header-bar">
    <h1>Exchange Resiliency Update</h1>
  </div>
</div>
<div class="content">
  <div id="table1" class="placeholder table-placeholder"></div>
</div>
</body>
</html>`);

  // Slide 6: Monolith Challenge
  fs.writeFileSync(path.join(workspace, 'slide6.html'), `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #F8F9FA; font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
}
.header { margin: 30pt 40pt 20pt 40pt; }
.header-bar { border-left: 8pt solid #F39C12; padding-left: 20pt; }
h1 { color: #1C2833; font-size: 32pt; margin: 0; font-weight: bold; }
.content { margin: 0 60pt 50pt 60pt; flex: 1; }
.callout {
  background: #ffffff;
  padding: 25pt;
  margin: 20pt 0;
  border-left: 6pt solid #E74C3C;
  border-radius: 4pt;
}
.callout-text { font-size: 20pt; color: #2C3E50; font-weight: bold; margin: 0; }
h2 { color: #2C3E50; font-size: 22pt; margin: 25pt 0 15pt 0; font-weight: bold; }
p { font-size: 16pt; color: #34495E; margin: 10pt 0; line-height: 1.4; }
</style>
</head>
<body>
<div class="header">
  <div class="header-bar">
    <h1>The Constraint: Breaking the Monolith</h1>
  </div>
</div>
<div class="content">
  <div class="callout">
    <p class="callout-text">Improvements will be incremental until we achieve Autonomous Teams</p>
  </div>
  <h2>What does "Autonomous Teams" mean?</h2>
  <p>Teams that can deploy independently, on demand, without coordinating with other teams - as long as no APIs, contracts, or data models are changed.</p>
</div>
</body>
</html>`);

  // Slide 7: Autonomous Teams Definition
  fs.writeFileSync(path.join(workspace, 'slide7.html'), `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #F8F9FA; font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
}
.header { margin: 25pt 40pt 10pt 40pt; }
.header-bar { border-left: 8pt solid #16A085; padding-left: 20pt; }
h1 { color: #1C2833; font-size: 26pt; margin: 0; font-weight: bold; }
.target { font-size: 14pt; color: #E74C3C; margin: 5pt 0 0 0; font-weight: bold; }
.content { margin: 0 60pt 50pt 60pt; flex: 1; }
h2 { color: #2C3E50; font-size: 16pt; margin: 12pt 0 6pt 0; font-weight: bold; }
ul { margin: 0; padding-left: 30pt; }
li { font-size: 12pt; color: #34495E; margin: 4pt 0; line-height: 1.2; }
</style>
</head>
<body>
<div class="header">
  <div class="header-bar">
    <h1>Phase 1 Definition of Done</h1>
  </div>
  <p class="target">Target: End of Q4 2026</p>
</div>
<div class="content">
  <h2>1. Org Change ✓</h2>
  <ul>
    <li>New team topology aligned to future decoupled architecture</li>
  </ul>
  <h2>2. Teams Correctly Staffed (In Progress)</h2>
  <ul>
    <li>Dedicated Engineering Manager</li>
    <li>Dedicated Product Owner</li>
    <li>Key roles filled</li>
  </ul>
  <h2>3. Clear Ownership</h2>
  <ul>
    <li>100% clear what each team owns (mutually exclusive, collectively exhaustive)</li>
  </ul>
  <h2>4. Independent Deployment</h2>
  <ul>
    <li>Code decoupled into standalone repos (or modular monolith)</li>
    <li>Teams own and operate deployment pipelines</li>
    <li>No coordination required for deployments</li>
  </ul>
</div>
</body>
</html>`);

  // Slide 8: Other Technical Work
  fs.writeFileSync(path.join(workspace, 'slide8.html'), `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #F8F9FA; font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
}
.header { margin: 30pt 40pt 20pt 40pt; }
.header-bar { border-left: 8pt solid #F39C12; padding-left: 20pt; }
h1 { color: #1C2833; font-size: 32pt; margin: 0; font-weight: bold; }
.content { margin: 0 50pt 50pt 50pt; flex: 1; display: flex; gap: 30pt; }
.left { flex: 1; }
.right { flex: 1; }
h2 { font-size: 17pt; margin: 0 0 15pt 0; font-weight: bold; }
.must-do h2 { color: #E74C3C; }
.negotiable h2 { color: #F39C12; }
ul { margin: 0; padding-left: 25pt; }
li { font-size: 13pt; color: #34495E; margin: 6pt 0; line-height: 1.3; }
.label { font-size: 11pt; color: #7F8C8D; margin: 5pt 0 0 0; font-style: italic; }
</style>
</head>
<body>
<div class="header">
  <div class="header-bar">
    <h1>Other Critical Technical Work</h1>
  </div>
</div>
<div class="content">
  <div class="left must-do">
    <h2>MUST DO (Cannot shift capacity until done)</h2>
    <p class="label">Data layer improvements:</p>
    <ul>
      <li>Move to cloud-native, infinitely scalable storage (DynamoDB, S3)</li>
      <li>Optimize read/write patterns</li>
      <li>Redirect dependencies to Common Data Platform (CDP)</li>
      <li>Thoughtful data retention policies</li>
    </ul>
    <p class="label">Benefits:</p>
    <ul>
      <li>Scalability</li>
      <li>Cost reduction</li>
      <li>HA/DR as a configuration setting</li>
    </ul>
  </div>
  <div class="right negotiable">
    <h2>REQUIRED BUT NEGOTIABLE (Timing flexible)</h2>
    <p class="label">Still urgent, but trade-offs possible:</p>
    <ul>
      <li>Event/Messaging system (replace Mongo-based Event Bus)</li>
      <li>Infinitely scalable queue processors/event subscribers (Lambdas)</li>
      <li>Cloud-native infra (containers, managed services vs EC2)</li>
      <li>Enhanced observability</li>
    </ul>
    <p class="label">Note: Veritas/Kickdrum will likely comment on these gaps</p>
  </div>
</div>
</body>
</html>`);

  // Slide 9: Timeline
  fs.writeFileSync(path.join(workspace, 'slide9.html'), `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #F8F9FA; font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
}
.header { margin: 25pt 40pt 15pt 40pt; }
.header-bar { border-left: 8pt solid #16A085; padding-left: 20pt; }
h1 { color: #1C2833; font-size: 28pt; margin: 0; font-weight: bold; }
.content { margin: 0 40pt 40pt 40pt; flex: 1; }
.timeline-placeholder { width: 100%; height: 300pt; }
</style>
</head>
<body>
<div class="header">
  <div class="header-bar">
    <h1>Timeline & Capacity Evolution</h1>
  </div>
</div>
<div class="content">
  <div id="timeline" class="placeholder timeline-placeholder"></div>
</div>
</body>
</html>`);
}

// Main function
async function createPresentation() {
  console.log('Creating gradient background...');
  await createGradientBackground();

  console.log('Creating HTML slides...');
  await createSlides();

  console.log('Converting to PowerPoint...');
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'Marten Engblom';
  pptx.title = 'Exchange Modernization Update - May 2026';

  // Slide 1: Cover
  await html2pptx(path.join(workspace, 'slide1.html'), pptx);

  // Slide 2: Agenda
  await html2pptx(path.join(workspace, 'slide2.html'), pptx);

  // Slide 3: Productivity with charts
  const { slide: slide3, placeholders: ph3 } = await html2pptx(path.join(workspace, 'slide3.html'), pptx);

  // Chart 1: Stories Completed
  slide3.addChart(pptx.charts.BAR, [{
    name: "Stories Completed",
    labels: ["January", "February", "March"],
    values: [207, 271, 386]
  }], {
    ...ph3[0],
    barDir: 'col',
    showTitle: true,
    title: 'Stories Completed (Jan-Mar)',
    showLegend: false,
    showCatAxisTitle: true,
    catAxisTitle: 'Month',
    showValAxisTitle: true,
    valAxisTitle: 'Stories',
    valAxisMaxVal: 400,
    valAxisMinVal: 0,
    chartColors: ["27AE60"]
  });

  // Chart 2: Lead Time & Cycle Time
  slide3.addChart(pptx.charts.LINE, [
    {
      name: "Lead Time (days)",
      labels: ["January", "February", "March"],
      values: [30, 33, 8]
    },
    {
      name: "Cycle Time (days)",
      labels: ["January", "February", "March"],
      values: [44, 44, 23]
    }
  ], {
    ...ph3[1],
    showTitle: true,
    title: 'Lead Time & Cycle Time Improvement',
    showLegend: true,
    legendPos: 'b',
    showCatAxisTitle: true,
    catAxisTitle: 'Month',
    showValAxisTitle: true,
    valAxisTitle: 'Days',
    valAxisMaxVal: 50,
    valAxisMinVal: 0,
    chartColors: ["16A085", "E74C3C"],
    lineSize: 3
  });

  // Slide 4: Other Improvements
  await html2pptx(path.join(workspace, 'slide4.html'), pptx);

  // Slide 5: Resiliency Table
  const { slide: slide5, placeholders: ph5 } = await html2pptx(path.join(workspace, 'slide5.html'), pptx);

  const tableData = [
    [
      { text: "Priority", options: { fill: { color: "1C2833" }, color: "FFFFFF", bold: true, fontSize: 14 } },
      { text: "Status", options: { fill: { color: "1C2833" }, color: "FFFFFF", bold: true, fontSize: 14 } },
      { text: "Notes", options: { fill: { color: "1C2833" }, color: "FFFFFF", bold: true, fontSize: 14 } }
    ],
    [
      "DB Migration to managed databases",
      { text: "On Track", options: { fill: { color: "27AE60" }, color: "FFFFFF", bold: true } },
      "Atlas Migration completion Aug 19"
    ],
    [
      "Disaster Recovery (4h RTO, 2h RPO)",
      { text: "On Track", options: { fill: { color: "27AE60" }, color: "FFFFFF", bold: true } },
      "Lower env test: RTO 7h, RPO 0:15h. Internal Oct, External Dec"
    ],
    [
      "All vulnerabilities within SLA / Eliminate EOL",
      { text: "Mixed", options: { fill: { color: "F39C12" }, color: "FFFFFF", bold: true } },
      "Red Mythos June 2 at risk, tracking July finish"
    ],
    [
      "Industry Continuity Solution",
      { text: "On Track", options: { fill: { color: "27AE60" }, color: "FFFFFF", bold: true } },
      "Building GHXi FTE team"
    ],
    [
      "Increase Modularity (Break the Monolith)",
      { text: "In Progress", options: { fill: { color: "16A085" }, color: "FFFFFF", bold: true } },
      '"Good enough" stage by end of Q4'
    ]
  ];

  slide5.addTable(tableData, {
    ...ph5[0],
    colW: [3.5, 1.5, 3.5],
    border: { pt: 1, color: "CCCCCC" },
    align: "left",
    valign: "middle",
    fontSize: 12
  });

  // Slide 6: Monolith Challenge
  await html2pptx(path.join(workspace, 'slide6.html'), pptx);

  // Slide 7: Autonomous Teams Definition
  await html2pptx(path.join(workspace, 'slide7.html'), pptx);

  // Slide 8: Other Technical Work
  await html2pptx(path.join(workspace, 'slide8.html'), pptx);

  // Slide 9: Timeline with Gantt-style bars
  const slide9 = await html2pptx(path.join(workspace, 'slide9.html'), pptx);

  // Timeline constants
  const startX = 2.2;
  const quarterWidth = 1.05;
  const rowHeight = 0.5;
  const startY = 1.3;
  const labelWidth = 2.0;

  const quarters = ["Q1 2026", "Q2 2026", "Q3 2026", "Q4 2026", "Q1 2027", "Q2 2027", "Q3 2027"];

  // Draw quarter headers
  quarters.forEach((q, i) => {
    slide9.slide.addText(q, {
      x: startX + (i * quarterWidth),
      y: startY - 0.4,
      w: quarterWidth,
      h: 0.3,
      fontSize: 10,
      bold: true,
      color: "2C3E50",
      align: "center"
    });
  });

  // Helper to draw rectangle bar with optional chevron taper
  function drawBar(slide, startQ, endQ, y, color, label, taperStart = null) {
    const x = startX + (startQ * quarterWidth);
    const fullWidth = (endQ - startQ) * quarterWidth;

    // Draw label
    slide.addText(label, {
      x: 0.3,
      y: y + 0.05,
      w: labelWidth,
      h: rowHeight - 0.1,
      fontSize: 11,
      color: "2C3E50",
      align: "left",
      valign: "middle"
    });

    if (taperStart === null) {
      // Simple rectangle - no taper
      slide.addShape(pptx.shapes.RECTANGLE, {
        x: x,
        y: y + 0.1,
        w: fullWidth,
        h: rowHeight - 0.2,
        fill: { color: color },
        line: { color: color, width: 0 }
      });
    } else {
      // Rectangle + chevron taper
      const fullPartWidth = (taperStart - startQ) * quarterWidth;
      const taperPartWidth = fullWidth - fullPartWidth;

      // Full intensity part
      if (fullPartWidth > 0) {
        slide.addShape(pptx.shapes.RECTANGLE, {
          x: x,
          y: y + 0.1,
          w: fullPartWidth,
          h: rowHeight - 0.2,
          fill: { color: color },
          line: { color: color, width: 0 }
        });
      }

      // Tapering part (right-pointing chevron)
      if (taperPartWidth > 0) {
        const chevronStartX = x + fullPartWidth;
        const chevY1 = y + 0.1;
        const chevY2 = y + (rowHeight / 2);
        const chevY3 = y + rowHeight - 0.1;
        const chevX2 = chevronStartX + taperPartWidth;

        // Draw as polygon using custom shape
        slide.addShape(pptx.shapes.RIGHT_ARROW, {
          x: chevronStartX,
          y: y + 0.1,
          w: taperPartWidth,
          h: rowHeight - 0.2,
          fill: { color: color },
          line: { color: color, width: 0 }
        });
      }
    }
  }

  // Work streams with Gantt bars
  let currentY = startY + 0.1;

  // MongoDB → Atlas (Q1-Q2, tapers in Q2)
  drawBar(slide9.slide, 0, 2, currentY, "16A085", "MongoDB → Atlas", 1.5);
  currentY += rowHeight;

  // Disaster Recovery (Q2-Q4, tapers in Q4)
  drawBar(slide9.slide, 1, 4, currentY, "27AE60", "Disaster Recovery", 3);
  currentY += rowHeight;

  // Red Mythos (Q2-Q3, tapers in Q3)
  drawBar(slide9.slide, 1, 3, currentY, "F39C12", "Red Mythos (Vuln/EOL)", 2.3);
  currentY += rowHeight;

  // Autonomous Teams (Q1-Q4)
  drawBar(slide9.slide, 0, 4, currentY, "E74C3C", "Autonomous Teams / Break Monolith", null);
  currentY += rowHeight;

  // P0 Database Improvements (Q4-Q2, tapers on both ends)
  drawBar(slide9.slide, 3.5, 6.5, currentY, "9B59B6", "P0 Database Improvements", null);
  currentY += rowHeight;

  // Other (Q2-Q3 2027)
  drawBar(slide9.slide, 5.5, 7, currentY, "95A5A6", "Other (Messaging, Infra)", null);
  currentY += rowHeight + 0.3;

  // Separator line
  slide9.slide.addShape(pptx.shapes.RECTANGLE, {
    x: 0.3,
    y: currentY,
    w: 9.4,
    h: 0.02,
    fill: { color: "CCCCCC" },
    line: { width: 0 }
  });
  currentY += 0.15;

  // Capacity row with colored boxes
  slide9.slide.addText("Capacity (Com/Tech)", {
    x: 0.3,
    y: currentY + 0.05,
    w: labelWidth,
    h: rowHeight - 0.1,
    fontSize: 11,
    bold: true,
    color: "2C3E50",
    align: "left",
    valign: "middle"
  });

  const capacityData = [
    { q: 0, val: "25/75", color: "E74C3C" },
    { q: 1, val: "25/75", color: "E74C3C" },
    { q: 2, val: "25/75", color: "E74C3C" },
    { q: 3, val: "25/75", color: "F39C12" },
    { q: 4, val: "50/50", color: "F39C12" },
    { q: 5, val: "50/50", color: "F39C12" },
    { q: 6, val: "70/30", color: "27AE60" }
  ];

  capacityData.forEach(cap => {
    const boxX = startX + (cap.q * quarterWidth) + (quarterWidth * 0.1);
    const boxW = quarterWidth * 0.8;

    slide9.slide.addShape(pptx.shapes.RECTANGLE, {
      x: boxX,
      y: currentY + 0.05,
      w: boxW,
      h: rowHeight - 0.1,
      fill: { color: cap.color },
      line: { width: 0 }
    });

    slide9.slide.addText(cap.val, {
      x: boxX,
      y: currentY + 0.05,
      w: boxW,
      h: rowHeight - 0.1,
      fontSize: 11,
      bold: true,
      color: "FFFFFF",
      align: "center",
      valign: "middle"
    });
  });

  // Save presentation
  const outputPath = '/Users/mengblom/Documents/ghx-dex/04-Projects/Exchange_Modernization_Report_May_2026/Presentations/Exchange-Modernization-Update-v4.pptx';
  await pptx.writeFile({ fileName: outputPath });
  console.log(`✓ Presentation saved: ${outputPath}`);
}

createPresentation().catch(console.error);
