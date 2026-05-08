const pptxgen = require('pptxgenjs');
const html2pptx = require('/Users/mengblom/Documents/ghx-dex/.claude/skills/anthropic-pptx/scripts/html2pptx.js');
const path = require('path');

async function createPresentation() {
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'Marten Engblom';
  pptx.title = 'CJ Strategic Update - Resiliency & Capacity Planning';

  // Slide 1: Executive Summary
  await html2pptx(path.join(__dirname, 'slide1.html'), pptx);

  // Slide 2: Productivity Data with dual-axis chart
  const { slide: slide2, placeholders: p2 } = await html2pptx(path.join(__dirname, 'slide2.html'), pptx);

  // Add productivity trend chart with dual axes
  // Stories Completed uses left axis (0-400)
  // Lead Time and Cycle Time use right axis (0-50 days)
  slide2.addChart(pptx.charts.BAR, [
    {
      name: 'Stories Completed',
      labels: ['Jan', 'Feb', 'Mar'],
      values: [207, 271, 386]
    }
  ], {
    x: p2[0].x,
    y: p2[0].y,
    w: p2[0].w,
    h: p2[0].h,
    barDir: 'col',
    showTitle: true,
    title: 'Productivity Trends (Jan - Mar 2026)',
    showLegend: true,
    legendPos: 'b',
    showCatAxisTitle: true,
    catAxisTitle: 'Month',
    showValAxisTitle: true,
    valAxisTitle: 'Stories Completed',
    chartColors: ['4472C4'],
    valAxisMaxVal: 400,
    valAxisMajorUnit: 100
  });

  // Note: PptxGenJS doesn't support dual-axis charts natively
  // The user will need to manually add the Lead Time/Cycle Time series with secondary axis in PowerPoint

  // Slide 3: Context & Ceiling
  await html2pptx(path.join(__dirname, 'slide3.html'), pptx);

  // Slide 4: Resiliency Priorities with updated table
  const { slide: slide4, placeholders: p4 } = await html2pptx(path.join(__dirname, 'slide4.html'), pptx);

  const tableData = [
    [
      { text: 'Priority', options: { fill: { color: '1C2833' }, color: 'FFFFFF', bold: true } },
      { text: 'Status', options: { fill: { color: '1C2833' }, color: 'FFFFFF', bold: true } },
      { text: 'Notes', options: { fill: { color: '1C2833' }, color: 'FFFFFF', bold: true } }
    ],
    ['DB Migration to Managed Databases', '🟢 On track', 'Atlas Migration completion Aug 29'],
    ['DR Test (RTO/RPO)', '🟢 On track', 'Lower environment test: RTO 4:45, RPO: 0:15, Internal target October, External comms December'],
    ['Red Mythos/Vulnerabilities', '🟡 Complex', 'Monolith dependencies - still targeting Q2'],
    ['EOL Technologies', '🟡 Complex', 'Atlas, Elasticsearch, Java upgrades, OSS upgrades'],
    ['ICS (Industry Continuity)', '🟢 On track', 'Building FTE team to own this'],
    ['Breaking the Monolith', '🟡 In progress', 'The big one (next slides)']
  ];

  slide4.addTable(tableData, {
    x: p4[0].x,
    y: p4[0].y,
    w: p4[0].w,
    h: p4[0].h,
    colW: [2.5, 1.5, 4.5],
    border: { pt: 1, color: 'CCCCCC' },
    align: 'left',
    valign: 'middle',
    fontSize: 10
  });

  // Slide 5: The Monolith Problem (updated - no costs)
  await html2pptx(path.join(__dirname, 'slide5.html'), pptx);

  // Slide 6: The Cost of the Monolith (NEW)
  await html2pptx(path.join(__dirname, 'slide6-new.html'), pptx);

  // Slide 7: Resiliency Endgame with expanded negotiables (formerly slide6)
  await html2pptx(path.join(__dirname, 'slide6.html'), pptx);

  // Slide 8: Current Progress (formerly slide7)
  await html2pptx(path.join(__dirname, 'slide7.html'), pptx);

  // Slide 9: Simplified Capacity Evolution (formerly slide8)
  const { slide: slide9, placeholders: p9 } = await html2pptx(path.join(__dirname, 'slide8.html'), pptx);

  // Create three simplified 2-section pie charts
  // Q2 - Baseline
  slide9.addChart(pptx.charts.PIE, [{
    name: 'Q2 2026 (Baseline)',
    labels: ['Technical Work (70%)', 'Commercial Roadmap (30%)'],
    values: [70, 30]
  }], {
    x: p9[0].x,
    y: p9[0].y + 0.3,
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
  slide9.addChart(pptx.charts.PIE, [{
    name: 'Q3 2026 (Transition)',
    labels: ['Technical Work (60%)', 'Commercial Roadmap (40%)'],
    values: [60, 40]
  }], {
    x: p9[0].x + 2.8,
    y: p9[0].y + 0.3,
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
  slide9.addChart(pptx.charts.PIE, [{
    name: 'Q4 2026 (Stabilized)',
    labels: ['Technical Work (50%)', 'Commercial Roadmap (50%)'],
    values: [50, 50]
  }], {
    x: p9[0].x + 5.6,
    y: p9[0].y + 0.3,
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

  // Slide 10: Org Chart (formerly slide9)
  await html2pptx(path.join(__dirname, 'slide9.html'), pptx);

  // Save presentation
  await pptx.writeFile({ fileName: path.join(__dirname, 'CJ-Strategic-Update.pptx') });
  console.log('Presentation created: CJ-Strategic-Update.pptx');
}

createPresentation().catch(err => {
  console.error('Error creating presentation:', err);
  process.exit(1);
});
