# Deploy IIUC Smart Library

1. Revoke the API key previously shared in chat and create a replacement at https://ollama.com/settings/keys .
2. Replace app.py and gemma_engine.py in your project with these matching versions. Keep iiuc_library_data.py and requirements.txt beside them.
3. Commit the changed code and .gitignore to your GitHub repository. Never commit a real key or .streamlit/secrets.toml. This package contains no real key or Git history.
4. At https://share.streamlit.io create an app, select your repository and branch, and choose app.py as the entrypoint. In Advanced settings choose Python 3.12.
5. Paste the following into Advanced settings > Secrets, replacing the placeholder privately:

```toml
OLLAMA_BACKEND = "cloud"
OLLAMA_MODEL = "gemma4:31b"
OLLAMA_API_KEY = "YOUR_NEW_KEY"
```

6. Deploy. If already deployed, update these values in App settings > Secrets and push the updated code.
7. Open the sidebar and click Check AI connection. This checks API reachability and the model list; it does not prove image inference or account quota is available.
8. Scan a clear book cover, then a portrait, then an unknown book. Non-book images must not yield a fabricated catalogue match. Model judgments can still be wrong; validate with your own images.
9. Test course search and study advice. Locations are sample catalogue data, not confirmed physical library records.

Cloud mode uses https://ollama.com/api/chat with server-side Bearer authentication. Your laptop and local Ollama do not need to stay running. Your account must have access and remaining usage for the chosen model. Uploaded images are sent to Ollama Cloud when analyzed.

## Local mode

For laptop testing, put this in .streamlit/secrets.toml (create the folder if needed):

```toml
OLLAMA_BACKEND = "local"
OLLAMA_MODEL = "gemma4:e2b"
OLLAMA_BASE_URL = "http://localhost:11434"
```

Run:

```bat
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Do not use local mode on Community Cloud unless a separately hosted backend is configured. Keep the example secrets file free of real credentials.

## Validation

Syntax, mocked authenticated text/image requests, non-book rejection, unknown-book handling, HTTP authentication/rate-limit errors are checked using simulated responses; Streamlit startup was not tested because Streamlit was unavailable in the editing environment. Real Ollama Cloud inference requires your replacement key and account and must be tested after configuration.

References: https://docs.ollama.com/cloud , https://docs.ollama.com/api/authentication , https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app .
