# SimpleOrderingSystem CRUD — Web Dashboard (Flask + Fetch)

This project adds a **new API + frontend layer** on top of your existing OOP CRUD backend.

## Run (Dev)
1. Install dependencies:
   - Ensure `Flask` is installed in your environment (see `requirements.txt`).
2. Start the server:
   ```bash
   python api/app.py
   ```
3. Open the dashboard in your browser:
   - http://127.0.0.1:5000/

## API Endpoints
- `GET /items`
- `POST /items`
- `PUT /items/<item_id>`
- `DELETE /items/<item_id>`

## Notes
- Frontend uses `fetch()` and updates the UI without full page reload.
- Data is still stored in `storage/data.json` via the existing persistence helper.

