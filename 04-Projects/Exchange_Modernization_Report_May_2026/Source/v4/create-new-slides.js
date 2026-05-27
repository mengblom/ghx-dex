const pptxgen = require('pptxgenjs');
const html2pptx = require('/Users/mengblom/Documents/ghx-dex/.claude/skills/anthropic-pptx/scripts/html2pptx.js');
const path = require('path');

async function createNewSlides() {
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'Marten Engblom';
  pptx.title = 'Exchange Modernization Update - New Slides';

  // Slide 1 (11 in full deck): Risks & Mitigations
  const { slide: slide11, placeholders: p11 } = await html2pptx(path.join(__dirname, 'slide11.html'), pptx);

  const risksData = [
    [
      { text: 'Initiative', options: { fill: { color: '1C2833' }, color: 'FFFFFF', bold: true } },
      { text: 'Risks', options: { fill: { color: '1C2833' }, color: 'FFFFFF', bold: true } },
      { text: 'Mitigations', options: { fill: { color: '1C2833' }, color: 'FFFFFF', bold: true } }
    ],
    [
      'MongoDB to Atlas',
      'Minimal Risk at this point',
      'No mitigation needed at this point'
    ],
    [
      'Disaster Recovery',
      'Unknown Unknowns, Outside dependencies on Exchange',
      'Discovery work started, lower env dry runs, targeting Oct vs Dec for buffer, engaging teams outside Exchange'
    ],
    [
      'Red Mythos',
      'High coupling → high complexity → big bang approach, large version jumps',
      'Sequestered team on dedicated branch/env, heavy AI use for remediation and testing, all hands plan for merging'
    ],
    [
      'Autonomous Teams / Break Monolith',
      'Impact from Atlas, DR, Red Mythos; Hiring (esp. India); High coupling; Unknown unknowns',
      'Fast-tracking DR and Red Mythos, India comp flexibility, giving teams flexibility on reaching independent deployments'
    ],
    [
      { text: 'COMMON RISK', options: { bold: true } },
      { text: 'Competing priorities & interference on same monolithic codebase', options: { bold: true } },
      { text: 'Laser focus Q3-Q4 (see next slide)', options: { bold: true } }
    ]
  ];

  slide11.addTable(risksData, {
    x: p11[0].x,
    y: p11[0].y,
    w: p11[0].w,
    h: p11[0].h,
    colW: [2.0, 3.0, 3.5],
    border: { pt: 1, color: 'CCCCCC' },
    align: 'left',
    valign: 'top',
    fontSize: 9
  });

  // Slide 2 (12 in full deck): Q3-Q4 Technical Laser Focus
  await html2pptx(path.join(__dirname, 'slide12.html'), pptx);

  // Save presentation
  const outputPath = path.join(__dirname, 'new-slides-11-12.pptx');
  await pptx.writeFile({ fileName: outputPath });
  console.log(`New slides saved: ${outputPath}`);
  console.log('\nTo add these to v4:');
  console.log('1. Open Exchange-Modernization-Update-v4.pptx');
  console.log('2. Open new-slides-11-12.pptx');
  console.log('3. Copy slides from new-slides-11-12.pptx and paste into v4');
  console.log('4. Save as Exchange-Modernization-Update-v5.pptx');
}

createNewSlides().catch(console.error);
