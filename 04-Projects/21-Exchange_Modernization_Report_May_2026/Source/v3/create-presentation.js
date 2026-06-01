const pptxgen = require('pptxgenjs');
const html2pptx = require('/Users/mengblom/Documents/ghx-dex/.claude/skills/anthropic-pptx/scripts/html2pptx.js');
const path = require('path');

async function createPresentation() {
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'Marten Engblom';
  pptx.title = 'CJ Strategic Update - Concise Version';

  // Slide 1: The Asks from CJ
  await html2pptx(path.join(__dirname, 'slide01.html'), pptx);

  // Slide 2: Executive Summary
  await html2pptx(path.join(__dirname, 'slide02.html'), pptx);

  // Slide 3: Productivity - Positive Signs (with chart)
  const { slide: slide3, placeholders: p3 } = await html2pptx(path.join(__dirname, 'slide03.html'), pptx);

  slide3.addChart(pptx.charts.BAR, [
    {
      name: 'Stories Completed',
      labels: ['Jan', 'Feb', 'Mar'],
      values: [207, 271, 386]
    }
  ], {
    x: p3[0].x,
    y: p3[0].y,
    w: p3[0].w,
    h: p3[0].h,
    barDir: 'col',
    showTitle: true,
    title: 'Productivity Trends (Jan - Mar 2026)',
    showLegend: false,
    showCatAxisTitle: true,
    catAxisTitle: 'Month',
    showValAxisTitle: true,
    valAxisTitle: 'Stories Completed',
    chartColors: ['4472C4'],
    valAxisMaxVal: 400,
    valAxisMajorUnit: 100
  });

  // Slide 4: Productivity - Challenges
  await html2pptx(path.join(__dirname, 'slide04.html'), pptx);

  // Slide 5: In Summary - Incremental Improvements
  await html2pptx(path.join(__dirname, 'slide05.html'), pptx);

  // Slide 6: Other Resiliency Priorities (with table)
  const { slide: slide6, placeholders: p6 } = await html2pptx(path.join(__dirname, 'slide06.html'), pptx);

  const tableData = [
    [
      { text: 'Priority', options: { fill: { color: '1C2833' }, color: 'FFFFFF', bold: true } },
      { text: 'Status', options: { fill: { color: '1C2833' }, color: 'FFFFFF', bold: true } },
      { text: 'Notes', options: { fill: { color: '1C2833' }, color: 'FFFFFF', bold: true } }
    ],
    ['DB Migration to Managed Databases', '🟢 On track', 'Atlas Migration completion Aug 29'],
    ['DR Test (RTO/RPO)', '🟢 On track', 'Lower environment test: RTO 4:45, RPO 0:15. Internal target October, External comms December'],
    ['Red Mythos/Vulnerabilities', '🟡 Complex', 'Monolith dependencies - targeting July 2 completion'],
    ['EOL Technologies', '🟡 Complex', 'Atlas, Elasticsearch, Java upgrades, OSS upgrades'],
    ['ICS (Industry Continuity)', '🟢 On track', 'Building FTE team to own this'],
    ['Breaking the Monolith', '🟡 In progress', 'The big one (next slides)']
  ];

  slide6.addTable(tableData, {
    x: p6[0].x,
    y: p6[0].y,
    w: p6[0].w,
    h: p6[0].h,
    colW: [2.5, 1.5, 4.5],
    border: { pt: 1, color: 'CCCCCC' },
    align: 'left',
    valign: 'middle',
    fontSize: 10
  });

  // Slide 7: The Monolith (placeholder)
  await html2pptx(path.join(__dirname, 'slide07.html'), pptx);

  // Slide 8: The Cost of the Monolith
  await html2pptx(path.join(__dirname, 'slide08.html'), pptx);

  // Slide 9: Monolith vs Services (placeholder)
  await html2pptx(path.join(__dirname, 'slide09.html'), pptx);

  // Slide 10: What Does Autonomous Teams Mean?
  await html2pptx(path.join(__dirname, 'slide10.html'), pptx);

  // Slide 11: When Are We Out of the Woods?
  await html2pptx(path.join(__dirname, 'slide11.html'), pptx);

  // Slide 12: Backlog of Work
  await html2pptx(path.join(__dirname, 'slide12.html'), pptx);

  // Slide 13: Capacity Evolution (with pie charts)
  const { slide: slide13, placeholders: p13 } = await html2pptx(path.join(__dirname, 'slide13.html'), pptx);

  // Q2 - Baseline
  slide13.addChart(pptx.charts.PIE, [{
    name: 'Q2 2026 (Baseline)',
    labels: ['Technical Work (70%)', 'Commercial Roadmap (30%)'],
    values: [70, 30]
  }], {
    x: p13[0].x,
    y: p13[0].y + 0.3,
    w: 2.5,
    h: 2.5,
    showTitle: true,
    title: 'Q2 2026 (Baseline)',
    titleFontSize: 12,
    showPercent: true,
    showLegend: false,
    chartColors: ['E74C3C', '2ECC71'],
    dataLabelPosition: 'bestFit',
    dataLabelFontSize: 10
  });

  // Q3 - Transition
  slide13.addChart(pptx.charts.PIE, [{
    name: 'Q3 2026 (Transition)',
    labels: ['Technical Work (60%)', 'Commercial Roadmap (40%)'],
    values: [60, 40]
  }], {
    x: p13[0].x + 2.8,
    y: p13[0].y + 0.3,
    w: 2.5,
    h: 2.5,
    showTitle: true,
    title: 'Q3 2026 (Transition)',
    titleFontSize: 12,
    showPercent: true,
    showLegend: false,
    chartColors: ['E74C3C', '2ECC71'],
    dataLabelPosition: 'bestFit',
    dataLabelFontSize: 10
  });

  // Q4 - Stabilized
  slide13.addChart(pptx.charts.PIE, [{
    name: 'Q4 2026 (Stabilized)',
    labels: ['Technical Work (50%)', 'Commercial Roadmap (50%)'],
    values: [50, 50]
  }], {
    x: p13[0].x + 5.6,
    y: p13[0].y + 0.3,
    w: 2.5,
    h: 2.5,
    showTitle: true,
    title: 'Q4 2026 (Stabilized)',
    titleFontSize: 12,
    showPercent: true,
    showLegend: false,
    chartColors: ['E74C3C', '2ECC71'],
    dataLabelPosition: 'bestFit',
    dataLabelFontSize: 10
  });

  // Save presentation
  await pptx.writeFile({ fileName: path.join(__dirname, 'CJ-Strategic-Update-v3.pptx') });
  console.log('Presentation created: CJ-Strategic-Update-v3.pptx (13 slides)');
}

createPresentation().catch(err => {
  console.error('Error creating presentation:', err);
  process.exit(1);
});
