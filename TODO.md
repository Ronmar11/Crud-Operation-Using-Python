# TODO - Flask API + Professional Frontend (No Backend Changes)

## Step 1: Verify dependencies
- [x] Read `requirements.txt` to check if Flask is already included. (Flask not listed; will require adding it.)


## Step 2: Add Flask API bridge (new files only)
- [x] Create `api/app.py` (or similar) serving:

  - `GET /items`
  - `POST /items`
  - `PUT /items/<id>`
  - `DELETE /items/<id>`
- [ ] Ensure persistence is done via existing `utils/file_handle.save_data(service.to_dicts())`.

## Step 3: Add frontend UI files
- [ ] Create `frontend/templates/index.html`
- [ ] Create `frontend/static/css/styles.css`
- [ ] Create `frontend/static/js/app.js`

## Step 4: Integrate UI with API
- [ ] Implement fetch-based CRUD with no page reload.
- [ ] Real-time UI updates after create/update/delete.
- [ ] Add modal forms for create/update.
- [ ] Add delete confirmation.

## Step 5: Polish + validate
- [ ] Ensure responsive layout works on mobile.
- [ ] Add basic error handling and loading states.
- [ ] Run Flask locally and validate endpoints.

