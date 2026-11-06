// Local search only. No accounts, tracking, or network service required.
const input = document.querySelector('#library-search');
if (input) {
  const results = document.querySelector('#search-results');
  let pages;
  let request;
  input.addEventListener('input', async () => {
    const query = input.value.trim().toLowerCase();
    if (query.length < 2) { results.replaceChildren(); return; }
    try {
      request ||= fetch('/search.json').then(r => { if (!r.ok) throw new Error(); return r.json(); });
      pages ||= await request;
      if (input.value.trim().toLowerCase() !== query) return;
      const matches = pages.filter(p => `${p.title} ${p.description} ${p.section}`.toLowerCase().includes(query));
      results.replaceChildren();
      const summary = document.createElement('p');
      summary.textContent = `${matches.length} result${matches.length === 1 ? '' : 's'}`;
      results.append(summary);
      for (const page of matches) {
        const link = document.createElement('a'); link.href = page.url;
        link.textContent = `${page.title} — ${page.description}`;
        results.append(link);
      }
    } catch { request = null; results.textContent = 'Search is unavailable. Use the navigation to browse the library.'; }
  });
}
