# Repository Inventory

## Current Files and Directories

### Python Files
- [x] `main.py` → Move to `bot/main.py` (✅ נשאר)
- [x] `check_balance.py` → Move to `bot/utils/` (✅ נשאר)
- [x] `requirements.txt` → Keep in root (✅ נשאר)
- [ ] `backend/` → Move to `_archive/2025-05-06/` (🗄️ ארכיון)

### Logs and Documentation
- [x] `swap_log.txt` → Move to `logs/` (✅ נשאר)
- [x] `swap_log_real.txt` → Move to `logs/` (✅ נשאר)
- [ ] `logs` → Move to `_archive/2025-05-06/` (🗄️ ארכיון)
- [ ] `איפה_עצרנו.txt` → Move to `_archive/2025-05-06/` (🗄️ ארכיון)

### Frontend
- [ ] `frontend` → Move to `_archive/2025-05-06/` (🗄️ ארכיון)
- [ ] `html` → Move to `_archive/2025-05-06/` (🗄️ ארכיון)

### Directories to Clean
- [ ] `__pycache__/` → Delete (❌ מחיקה)
- [ ] `.git/` → Keep (✅ נשאר)

## New Structure
```
SEMD-Project/
├─ contracts/          # For future Solana contracts
├─ bot/
│  ├─ __init__.py     # Empty file for proper Python imports
│  ├─ main.py         # Main entry point
│  ├─ solana_swap.py  # New swap implementation
│  └─ utils/          # Utility functions
├─ dashboard/         # New Next.js frontend
├─ infra/
│  ├─ Dockerfile
│  └─ k8s/
├─ tests/
├─ docs/             # Documentation
└─ README.md         # Project documentation (to be updated)
```

## Action Items
1. Create archive directory with today's date:
   ```
   _archive/2025-05-06/
   ```

2. Move files to archive:
   - [ ] `backend/` → `_archive/2025-05-06/backend/`
   - [ ] `frontend` → `_archive/2025-05-06/frontend/`
   - [ ] `html` → `_archive/2025-05-06/html/`
   - [ ] `logs` → `_archive/2025-05-06/logs/`
   - [ ] `איפה_עצרנו.txt` → `_archive/2025-05-06/`

3. Delete unnecessary files:
   - [ ] `__pycache__/` directory and all contents

4. Verify final structure:
   - [ ] All Python files in correct locations
   - [ ] All logs in `logs/` directory
   - [ ] No duplicate files
   - [ ] No unnecessary cache files

## Next Steps
1. Create new directory structure
2. Move existing files to appropriate locations
3. Create placeholder files for new structure
4. Update README.md with new project information 

✔️ Python 3.12 פעיל 