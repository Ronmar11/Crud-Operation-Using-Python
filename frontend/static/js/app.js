// App entry: manage UI state and communicate with Flask API using Fetch API.
// This file implements SPA-like behavior without page reloads.
(function () {
  const wrapper = document.getElementById('wrapper');
  const menuToggle = document.getElementById('menu-toggle');
  const navLinks = Array.from(document.querySelectorAll('[data-nav]'));
  const dashboardSection = document.getElementById('dashboard-section');
  const itemsSection = document.getElementById('items-section');
  const settingsSection = document.getElementById('settings-section');
  const searchInput = document.getElementById('search');
  const itemsContainer = document.getElementById('items-container');
  const totalItems = document.getElementById('total-items');
  const openCreate = document.getElementById('open-create');
  const itemForm = document.getElementById('item-form');
  const itemModalEl = document.getElementById('itemModal');
  const itemModal = new bootstrap.Modal(itemModalEl);
  const confirmModal = new bootstrap.Modal(document.getElementById('confirmModal'));
  const confirmYes = document.getElementById('confirmYes');

  let items = [];
  let editingId = null;
  let pendingDeleteId = null;
  let activeView = 'dashboard';

  async function api(path, opts = {}) {
    const res = await fetch(
      path,
      Object.assign({ headers: { 'Content-Type': 'application/json' } }, opts)
    );
    if (!res.ok) throw new Error(await res.text());
    return res.json();
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, (char) => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;'
    }[char]));
  }

  function filterItems(query) {
    const normalized = String(query || '').trim().toLowerCase();
    if (!normalized) return items;
    return items.filter((item) => String(item.name || '').toLowerCase().includes(normalized));
  }

  function setActiveView(view) {
    activeView = view;

    dashboardSection.classList.toggle('section-hidden', view === 'settings');
    itemsSection.classList.toggle('section-hidden', view === 'settings');
    settingsSection.classList.toggle('section-hidden', view !== 'settings');

    navLinks.forEach((link) => {
      link.classList.toggle('active', link.dataset.nav === view);
    });

    if (view === 'settings') {
      searchInput.value = '';
    }
  }

  function renderItems(list) {
    itemsContainer.innerHTML = '';
    totalItems.textContent = String(list.length);

    if (!list.length) {
      itemsContainer.innerHTML = `
        <div class="col-12">
          <div class="alert alert-light border mb-0">No items found.</div>
        </div>`;
      return;
    }

    list.forEach((item) => {
      const col = document.createElement('div');
      col.className = 'col-sm-6 col-md-4 col-lg-3';
      const imageMarkup = item.image_url
        ? `<img class="item-image" src="${escapeHtml(item.image_url)}" alt="${escapeHtml(item.name)}" loading="lazy" onerror="this.onerror=null;this.src='/static/img/item-placeholder.svg'">`
        : `<div class="item-image item-image-placeholder">No image</div>`;
      col.innerHTML = `
        <div class="item-card">
          ${imageMarkup}
          <div class="d-flex justify-content-between align-items-start mb-2">
            <strong>${escapeHtml(item.name)}</strong>
            <div class="text-end">
              <div class="meta">ID: ${item.item_id}</div>
              <div class="meta">$${Number(item.price).toFixed(2)}</div>
            </div>
          </div>
          <div class="mt-auto d-flex gap-2">
            <button class="btn btn-outline-secondary btn-sm edit-btn" data-id="${item.item_id}">Edit</button>
            <button class="btn btn-outline-danger btn-sm delete-btn" data-id="${item.item_id}">Delete</button>
          </div>
        </div>`;
      itemsContainer.appendChild(col);
    });

    document.querySelectorAll('.edit-btn').forEach((button) => button.addEventListener('click', onEdit));
    document.querySelectorAll('.delete-btn').forEach((button) => button.addEventListener('click', onDelete));
  }

  async function loadItems() {
    try {
      items = await api('/api/items');
      renderItems(filterItems(searchInput.value));
    } catch (error) {
      console.error('Failed to load items', error);
      itemsContainer.innerHTML = `
        <div class="col-12">
          <div class="alert alert-danger mb-0">Failed to load items from the backend.</div>
        </div>`;
    }
  }

  function onEdit(event) {
    const id = Number(event.currentTarget.dataset.id);
    const item = items.find((currentItem) => currentItem.item_id === id);
    if (!item) return;

    editingId = id;
    itemForm.item_id.value = item.item_id;
    itemForm.name.value = item.name;
    itemForm.price.value = item.price;
    itemForm.image_url.value = item.image_url || '';
    itemForm.item_id.disabled = true;
    itemModalEl.querySelector('.modal-title').textContent = 'Update Item';
    itemModal.show();
  }

  function onDelete(event) {
    pendingDeleteId = Number(event.currentTarget.dataset.id);
    document.getElementById('confirmText').textContent = `Delete item ${pendingDeleteId}?`;
    confirmModal.show();
  }

  navLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      setActiveView(link.dataset.nav);

      if (link.dataset.nav === 'dashboard') {
        loadItems();
      }

      if (link.dataset.nav === 'items') {
        renderItems(filterItems(searchInput.value));
      }
    });
  });

  menuToggle.addEventListener('click', () => {
    wrapper.classList.toggle('sidebar-collapsed');
  });

  searchInput.addEventListener('input', () => {
    if (activeView !== 'settings') {
      renderItems(filterItems(searchInput.value));
    }
  });

  confirmYes.addEventListener('click', async () => {
    if (!pendingDeleteId) return;

    try {
      await api(`/api/items/${pendingDeleteId}`, { method: 'DELETE' });
      pendingDeleteId = null;
      confirmModal.hide();
      await loadItems();
    } catch (error) {
      console.error(error);
      alert('Unable to delete item.');
    }
  });

  openCreate.addEventListener('click', () => {
    editingId = null;
    itemForm.reset();
    itemForm.item_id.disabled = false;
    itemModalEl.querySelector('.modal-title').textContent = 'Create Item';
    itemModal.show();
  });

  itemForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const payload = {
      item_id: Number(itemForm.item_id.value),
      name: itemForm.name.value.trim(),
      price: Number(itemForm.price.value),
      image_url: itemForm.image_url.value.trim(),
    };

    try {
      if (editingId) {
        await api(`/api/items/${editingId}`, {
          method: 'PUT',
          body: JSON.stringify(payload),
        });
      } else {
        await api('/api/items', {
          method: 'POST',
          body: JSON.stringify(payload),
        });
      }

      itemModal.hide();
      await loadItems();
    } catch (error) {
      console.error(error);
      alert('Error: ' + error.message);
    }
  });

  setActiveView('dashboard');
  loadItems();
})();
