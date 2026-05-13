#!/usr/bin/env python3
"""Add Flashcard mode tab."""

with open('/home/user/IV/senior-architect-prep.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ══════════════════════════════════════════════════════════════════════
# STEP 1 — CSS for flashcard UI
# ══════════════════════════════════════════════════════════════════════
fc_css = """
  /* ===== FLASHCARD MODE ===== */
  .fc-wrap { max-width: 820px; margin: 0 auto; }
  .fc-toolbar {
    display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
    margin-bottom: 18px; padding-bottom: 14px; border-bottom: 1px solid var(--border);
  }
  .fc-filter-btn {
    font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 700;
    text-transform: uppercase; letter-spacing: .08em;
    padding: 5px 12px; border-radius: 20px; border: 1px solid var(--border);
    background: transparent; color: var(--text-muted); cursor: pointer;
    transition: all .15s;
  }
  .fc-filter-btn:hover { border-color: var(--accent); color: var(--accent); }
  .fc-filter-btn.active { background: var(--accent); color: #000; border-color: var(--accent); }
  .fc-filter-btn.b.active { background: var(--info); border-color: var(--info); }
  .fc-filter-btn.r.active { background: var(--crit); border-color: var(--crit); }
  .fc-shuffle-btn {
    font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 700;
    text-transform: uppercase; letter-spacing: .08em;
    padding: 5px 12px; border-radius: 20px; border: 1px solid var(--border);
    background: var(--bg-elev); color: var(--text-muted); cursor: pointer;
    margin-left: auto; transition: all .15s;
  }
  .fc-shuffle-btn:hover { border-color: var(--accent); color: var(--accent); }
  .fc-progress-row {
    display: flex; align-items: center; gap: 10px; margin-bottom: 18px;
  }
  .fc-progress-track {
    flex: 1; height: 6px; background: var(--bg-elev); border-radius: 3px; overflow: hidden;
  }
  .fc-progress-fill { height: 100%; background: var(--accent); border-radius: 3px; transition: width .3s; }
  .fc-counter { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted); white-space: nowrap; }
  .fc-score-row {
    display: flex; gap: 8px; font-family: 'JetBrains Mono', monospace; font-size: 11px; flex-wrap: wrap;
  }
  .fc-score { padding: 2px 9px; border-radius: 12px; font-weight: 700; font-size: 10px; }
  .fc-score.ok   { background: rgba(74,222,128,.2);  color: var(--done); }
  .fc-score.shaky{ background: rgba(251,191,36,.2);  color: var(--warn); }
  .fc-score.miss { background: rgba(248,113,113,.2); color: var(--crit); }

  /* The card */
  .fc-card-wrap {
    perspective: 1200px; min-height: 300px; margin-bottom: 20px; cursor: pointer;
  }
  .fc-card-inner {
    position: relative; width: 100%; min-height: 300px;
    transform-style: preserve-3d; transition: transform .45s ease;
  }
  .fc-card-inner.flipped { transform: rotateY(180deg); }
  .fc-face {
    position: absolute; width: 100%; min-height: 300px;
    backface-visibility: hidden; -webkit-backface-visibility: hidden;
    border-radius: 14px; padding: 28px 32px;
    display: flex; flex-direction: column; justify-content: center;
    border: 1px solid var(--border);
  }
  .fc-front {
    background: var(--bg-card);
    border-top: 4px solid var(--accent);
  }
  .fc-front.high { border-top-color: var(--info); }
  .fc-front.med  { border-top-color: var(--done); }
  .fc-back {
    background: var(--bg-elev);
    transform: rotateY(180deg);
    border-top: 4px solid var(--done);
    overflow-y: auto; max-height: 600px;
    justify-content: flex-start;
    position: absolute; backface-visibility: hidden;
  }
  .fc-tag {
    font-family: 'JetBrains Mono', monospace; font-size: 9px; font-weight: 700;
    text-transform: uppercase; letter-spacing: .14em;
    color: var(--text-muted); margin-bottom: 14px; display: block;
  }
  .fc-tag.crit { color: var(--accent); }
  .fc-tag.high { color: var(--info); }
  .fc-tag.med  { color: var(--done); }
  .fc-question {
    font-family: 'Fraunces', serif; font-size: 20px; font-weight: 600; line-height: 1.45;
    color: var(--text);
  }
  .fc-hint {
    margin-top: 20px; font-family: 'JetBrains Mono', monospace; font-size: 10px;
    color: var(--text-muted); text-align: center; letter-spacing: .08em;
  }
  .fc-answer {
    font-size: 13px; line-height: 1.65; color: var(--text-dim);
  }
  .fc-answer strong { color: var(--text); }
  .fc-answer code {
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    background: var(--bg-deep); padding: 1px 5px; border-radius: 3px;
    color: var(--accent);
  }
  .fc-answer h4 { color: var(--accent); font-size: 13px; margin: 12px 0 4px; }
  .fc-answer ul, .fc-answer ol { padding-left: 18px; margin: 6px 0; }
  .fc-answer li { margin: 3px 0; }
  .fc-answer table { width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 11.5px; }
  .fc-answer th { background: var(--bg-deep); padding: 5px 8px; text-align: left; color: var(--text-muted); font-weight: 600; }
  .fc-answer td { padding: 4px 8px; border-bottom: 1px solid var(--border); }
  .fc-answer hr { border-color: var(--border); margin: 10px 0; }
  .fc-answer .tradeoff { color: var(--warn); font-weight: 600; }
  .fc-answer .gotcha { color: var(--crit); font-weight: 600; }
  .fc-answer pre { background: #04080d; border: 1px solid #16202e; border-radius: 6px; padding: 10px 12px; overflow-x: auto; font-family: 'JetBrains Mono', monospace; font-size: 10.5px; line-height: 1.65; color: var(--text-dim); white-space: pre-wrap; }

  /* Rating buttons */
  .fc-rate-row {
    display: flex; gap: 10px; margin-bottom: 20px;
  }
  .fc-rate-btn {
    flex: 1; padding: 12px; border-radius: 10px; border: 2px solid;
    font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700;
    cursor: pointer; transition: all .15s; display: flex; flex-direction: column;
    align-items: center; gap: 3px;
  }
  .fc-rate-btn span { font-size: 9px; font-weight: 400; opacity: .8; }
  .fc-rate-btn.ok    { border-color: var(--done); color: var(--done); background: rgba(74,222,128,.08); }
  .fc-rate-btn.shaky { border-color: var(--warn); color: var(--warn); background: rgba(251,191,36,.08); }
  .fc-rate-btn.miss  { border-color: var(--crit); color: var(--crit); background: rgba(248,113,113,.08); }
  .fc-rate-btn.ok:hover    { background: rgba(74,222,128,.25); }
  .fc-rate-btn.shaky:hover { background: rgba(251,191,36,.25); }
  .fc-rate-btn.miss:hover  { background: rgba(248,113,113,.25); }
  .fc-rate-row[style*="none"] + .fc-nav-row { margin-top: 0; }

  /* Nav */
  .fc-nav-row { display: flex; gap: 10px; align-items: center; justify-content: center; }
  .fc-nav-btn {
    font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 700;
    padding: 8px 20px; border-radius: 8px; border: 1px solid var(--border);
    background: var(--bg-elev); color: var(--text); cursor: pointer; transition: all .15s;
    letter-spacing: .04em;
  }
  .fc-nav-btn:hover { border-color: var(--accent); color: var(--accent); }
  .fc-nav-btn:disabled { opacity: .35; cursor: default; }
  .fc-flip-btn {
    font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700;
    padding: 10px 28px; border-radius: 8px; border: 2px solid var(--accent);
    background: var(--accent-soft); color: var(--accent); cursor: pointer; transition: all .15s;
    letter-spacing: .06em;
  }
  .fc-flip-btn:hover { background: var(--accent); color: #000; }

  /* Session summary */
  .fc-summary {
    text-align: center; padding: 40px 24px;
    border: 1px solid var(--border); border-radius: 14px; background: var(--bg-card);
  }
  .fc-summary h2 {
    font-family: 'Fraunces', serif; font-size: 28px; color: var(--text); margin-bottom: 10px;
  }
  .fc-summary-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 14px; margin: 24px 0; }
  .fc-summary-stat {
    padding: 16px; border-radius: 10px; border: 1px solid var(--border);
  }
  .fc-summary-stat .num { font-size: 32px; font-weight: 700; font-family: 'Fraunces', serif; }
  .fc-summary-stat .lbl { font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--text-muted); text-transform: uppercase; letter-spacing: .1em; margin-top: 4px; }
  .fc-summary-stat.ok   { background: rgba(74,222,128,.07);  border-color: rgba(74,222,128,.3); }
  .fc-summary-stat.ok .num { color: var(--done); }
  .fc-summary-stat.shaky{ background: rgba(251,191,36,.07);  border-color: rgba(251,191,36,.3); }
  .fc-summary-stat.shaky .num { color: var(--warn); }
  .fc-summary-stat.miss { background: rgba(248,113,113,.07); border-color: rgba(248,113,113,.3); }
  .fc-summary-stat.miss .num { color: var(--crit); }
  .fc-restart-btn {
    font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700;
    padding: 12px 32px; border-radius: 10px; border: 2px solid var(--accent);
    background: var(--accent); color: #000; cursor: pointer; margin: 6px;
    letter-spacing: .06em; transition: opacity .15s;
  }
  .fc-restart-btn:hover { opacity: .85; }
  .fc-restart-btn.sec {
    background: transparent; color: var(--crit); border-color: var(--crit);
  }
  .fc-empty { text-align: center; padding: 60px 20px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace; font-size: 13px; }
"""

content = content.replace('</style>\n</head>', fc_css + '</style>\n</head>', 1)
print("✓ Added Flashcard CSS")

# ══════════════════════════════════════════════════════════════════════
# STEP 2 — Add tab button
# ══════════════════════════════════════════════════════════════════════
old_btn = '    <button class="tab-btn" data-tab="quickprep">⚡ Quick Prep</button>'
new_btn = '''    <button class="tab-btn" data-tab="quickprep">⚡ Quick Prep</button>
    <button class="tab-btn" data-tab="flashcards">🃏 Flash</button>'''

if old_btn in content:
    content = content.replace(old_btn, new_btn, 1)
    print("✓ Added Flash tab button")
else:
    print("✗ Could not find quickprep button")

# ══════════════════════════════════════════════════════════════════════
# STEP 3 — Add Flashcard tab pane (static HTML shell, JS fills it)
# ══════════════════════════════════════════════════════════════════════
fc_pane = '''
  <div class="tab-pane" id="tab-flashcards">
    <div class="fc-wrap">
      <!-- toolbar -->
      <div class="fc-toolbar">
        <button class="fc-filter-btn active" data-fc-filter="all">All cards</button>
        <button class="fc-filter-btn r" data-fc-filter="crit">Must-know only</button>
        <button class="fc-filter-btn b" data-fc-filter="missed">Missed / Shaky</button>
        <button class="fc-shuffle-btn" id="fcShuffle">&#x21ba; Shuffle</button>
      </div>
      <!-- progress -->
      <div class="fc-progress-row">
        <div class="fc-progress-track"><div class="fc-progress-fill" id="fcFill" style="width:0%"></div></div>
        <span class="fc-counter" id="fcCounter">— / —</span>
      </div>
      <div class="fc-score-row" id="fcScoreRow" style="margin-bottom:16px"></div>
      <!-- card -->
      <div id="fcCardArea"></div>
      <!-- rate -->
      <div class="fc-rate-row" id="fcRateRow" style="display:none">
        <button class="fc-rate-btn ok"    data-rate="ok">✓ Got it<span>I could explain this</span></button>
        <button class="fc-rate-btn shaky" data-rate="shaky">~ Shaky<span>Partial / not fluent</span></button>
        <button class="fc-rate-btn miss"  data-rate="miss">✗ Missed<span>Blank / wrong</span></button>
      </div>
      <!-- nav -->
      <div class="fc-nav-row" id="fcNavRow">
        <button class="fc-nav-btn" id="fcPrev">&#x2190; Prev</button>
        <button class="fc-flip-btn" id="fcFlip">Flip to answer</button>
        <button class="fc-nav-btn" id="fcNext">Next &#x2192;</button>
      </div>
    </div>
  </div><!-- /tab-pane#flashcards -->
'''

old_anchor = '  </div><!-- /tab-pane#quickprep -->'
if old_anchor in content:
    content = content.replace(old_anchor, '  </div><!-- /tab-pane#quickprep -->' + fc_pane, 1)
    print("✓ Added Flashcard tab pane")
else:
    print("✗ Could not find quickprep pane end")

# ══════════════════════════════════════════════════════════════════════
# STEP 4 — Add Flashcard JS (before </script>)
# ══════════════════════════════════════════════════════════════════════
fc_js = r"""
// ============================================================
// FLASHCARD MODE
// ============================================================
(function initFlashcards() {
  // ── extract all Q&A pairs from DATA ──
  const allCards = [];
  DATA.forEach(block => {
    block.sections.forEach(sec => {
      if (!sec.items) return;
      sec.items.forEach(item => {
        if (item.q && item.a) {
          allCards.push({
            q: item.q,
            a: item.a,
            tag: item.tag || 'med',
            section: block.title,
            rating: null  // null | 'ok' | 'shaky' | 'miss'
          });
        }
      });
    });
  });

  let deck = [];          // active filtered+shuffled deck
  let idx = 0;            // current position in deck
  let flipped = false;
  let filterMode = 'all'; // 'all' | 'crit' | 'missed'

  function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  function buildDeck() {
    let source = allCards;
    if (filterMode === 'crit')   source = allCards.filter(c => c.tag === 'crit');
    if (filterMode === 'missed') source = allCards.filter(c => c.rating === 'miss' || c.rating === 'shaky');
    deck = shuffle([...source]);
    idx = 0;
    flipped = false;
  }

  function renderScores() {
    const ok    = allCards.filter(c => c.rating === 'ok').length;
    const shaky = allCards.filter(c => c.rating === 'shaky').length;
    const miss  = allCards.filter(c => c.rating === 'miss').length;
    const rated = ok + shaky + miss;
    const el = document.getElementById('fcScoreRow');
    if (!el) return;
    if (rated === 0) { el.innerHTML = ''; return; }
    el.innerHTML =
      `<span class="fc-score ok">&#x2713; ${ok} got it</span>` +
      `<span class="fc-score shaky">~ ${shaky} shaky</span>` +
      `<span class="fc-score miss">&#x2717; ${miss} missed</span>` +
      `<span style="font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);margin-left:4px">${rated}/${allCards.length} rated</span>`;
  }

  function renderProgress() {
    const fill   = document.getElementById('fcFill');
    const counter= document.getElementById('fcCounter');
    if (!fill || !counter) return;
    const pct = deck.length ? Math.round(((idx) / deck.length) * 100) : 0;
    fill.style.width = pct + '%';
    counter.textContent = deck.length ? `${idx + 1} / ${deck.length}` : '0 / 0';
  }

  function renderSummary() {
    const ok    = deck.filter(c => c.rating === 'ok').length;
    const shaky = deck.filter(c => c.rating === 'shaky').length;
    const miss  = deck.filter(c => c.rating === 'miss').length;
    const pct   = Math.round((ok / deck.length) * 100);
    const grade = pct >= 80 ? '&#x1f3c6; Ready' : pct >= 60 ? '&#x26a1; Almost' : '&#x1f4aa; Keep going';
    document.getElementById('fcCardArea').innerHTML = `
      <div class="fc-summary">
        <h2>${grade}</h2>
        <p style="font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--text-muted)">
          Session complete — ${deck.length} cards, ${pct}% confident
        </p>
        <div class="fc-summary-grid">
          <div class="fc-summary-stat ok">
            <div class="num">${ok}</div>
            <div class="lbl">Got it</div>
          </div>
          <div class="fc-summary-stat shaky">
            <div class="num">${shaky}</div>
            <div class="lbl">Shaky</div>
          </div>
          <div class="fc-summary-stat miss">
            <div class="num">${miss}</div>
            <div class="lbl">Missed</div>
          </div>
        </div>
        <button class="fc-restart-btn" id="fcRestartAll">Restart all cards</button>
        ${miss + shaky > 0 ? `<button class="fc-restart-btn sec" id="fcRestartWeak">Drill weak cards (${miss + shaky})</button>` : ''}
      </div>`;
    document.getElementById('fcRateRow').style.display = 'none';
    document.getElementById('fcNavRow').style.display  = 'none';
    document.getElementById('fcFill').style.width = '100%';
    document.getElementById('fcCounter').textContent = `${deck.length} / ${deck.length}`;

    const ra = document.getElementById('fcRestartAll');
    if (ra) ra.addEventListener('click', () => { buildDeck(); renderCard(); });
    const rw = document.getElementById('fcRestartWeak');
    if (rw) rw.addEventListener('click', () => {
      filterMode = 'missed'; buildDeck(); renderCard();
    });
  }

  function renderCard() {
    const area    = document.getElementById('fcCardArea');
    const rateRow = document.getElementById('fcRateRow');
    const navRow  = document.getElementById('fcNavRow');
    const prevBtn = document.getElementById('fcPrev');
    const nextBtn = document.getElementById('fcNext');
    const flipBtn = document.getElementById('fcFlip');
    if (!area) return;

    if (deck.length === 0) {
      area.innerHTML = `<div class="fc-empty">No cards match this filter.<br>Try "All cards" or rate some questions first.</div>`;
      rateRow.style.display = 'none';
      navRow.style.display  = 'none';
      renderProgress();
      renderScores();
      return;
    }

    if (idx >= deck.length) { renderSummary(); renderScores(); return; }

    const card = deck[idx];
    flipped = false;

    area.innerHTML = `
      <div class="fc-card-wrap" id="fcCardWrap">
        <div class="fc-card-inner" id="fcCardInner">
          <div class="fc-face fc-front ${card.tag}">
            <span class="fc-tag ${card.tag}">${card.tag === 'crit' ? '&#x26a1; Must-know' : card.tag === 'high' ? '&#x25b2; High' : '&#x25a0; Medium'} &nbsp;&#xb7;&nbsp; ${card.section}</span>
            <div class="fc-question">${card.q}</div>
            <div class="fc-hint">Click the card or "Flip" to reveal the answer</div>
          </div>
          <div class="fc-face fc-back">
            <span class="fc-tag ${card.tag}" style="margin-bottom:12px">${card.tag === 'crit' ? '&#x26a1; Must-know' : card.tag === 'high' ? '&#x25b2; High' : '&#x25a0; Medium'} &nbsp;&#xb7;&nbsp; ${card.section}</span>
            <div class="fc-answer">${card.a}</div>
          </div>
        </div>
      </div>`;

    rateRow.style.display = 'none';
    navRow.style.display  = 'flex';
    if (flipBtn) flipBtn.textContent = 'Flip to answer';
    if (prevBtn) prevBtn.disabled = (idx === 0);
    if (nextBtn) nextBtn.textContent = idx === deck.length - 1 ? 'Finish' : 'Next →';

    document.getElementById('fcCardWrap').addEventListener('click', doFlip);
    renderProgress();
    renderScores();
  }

  function doFlip() {
    if (flipped) return;
    flipped = true;
    const inner = document.getElementById('fcCardInner');
    if (inner) inner.classList.add('flipped');
    const rateRow = document.getElementById('fcRateRow');
    const flipBtn = document.getElementById('fcFlip');
    if (rateRow) rateRow.style.display = 'flex';
    if (flipBtn) flipBtn.textContent   = 'Flipped';
  }

  // ── wire events ──
  document.getElementById('fcFlip').addEventListener('click', doFlip);

  document.getElementById('fcNext').addEventListener('click', () => {
    idx++;
    if (idx >= deck.length) { renderSummary(); renderScores(); return; }
    renderCard();
  });

  document.getElementById('fcPrev').addEventListener('click', () => {
    if (idx > 0) { idx--; renderCard(); }
  });

  document.querySelectorAll('[data-rate]').forEach(btn => {
    btn.addEventListener('click', e => {
      const rate = e.currentTarget.dataset.rate;
      deck[idx].rating = rate;
      // also update in allCards array
      const orig = allCards.find(c => c.q === deck[idx].q);
      if (orig) orig.rating = rate;
      idx++;
      if (idx >= deck.length) { renderSummary(); renderScores(); return; }
      renderCard();
    });
  });

  document.querySelectorAll('[data-fc-filter]').forEach(btn => {
    btn.addEventListener('click', e => {
      document.querySelectorAll('[data-fc-filter]').forEach(b => b.classList.remove('active'));
      e.currentTarget.classList.add('active');
      filterMode = e.currentTarget.dataset.fcFilter;
      buildDeck(); renderCard();
    });
  });

  document.getElementById('fcShuffle').addEventListener('click', () => {
    buildDeck(); renderCard();
  });

  // ── keyboard shortcuts ──
  document.addEventListener('keydown', e => {
    if (document.getElementById('tab-flashcards').style.display === 'none') return;
    if (document.getElementById('tab-flashcards').classList.contains('active') === false) return;
    if (e.key === ' ' || e.key === 'f') { e.preventDefault(); doFlip(); }
    if (e.key === 'ArrowRight' || e.key === 'n') document.getElementById('fcNext').click();
    if (e.key === 'ArrowLeft'  || e.key === 'p') document.getElementById('fcPrev').click();
    if (e.key === '1') document.querySelector('[data-rate="ok"]').click();
    if (e.key === '2') document.querySelector('[data-rate="shaky"]').click();
    if (e.key === '3') document.querySelector('[data-rate="miss"]').click();
  });

  buildDeck();
  renderCard();
})();
"""

# Insert before closing </script>
old_end = '\n</script>\n</body>'
if old_end in content:
    content = content.replace(old_end, fc_js + '\n</script>\n</body>', 1)
    print("✓ Added Flashcard JS")
else:
    print("✗ Could not find </script>")

with open('/home/user/IV/senior-architect-prep.html', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"✓ Written — {content.count(chr(10))} lines")
