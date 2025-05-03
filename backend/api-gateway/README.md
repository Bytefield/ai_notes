✅ Purpose:
Acts as a central router that proxies requests from the frontend to the appropriate backend microservice.

📦 Endpoints:
POST /api/summarize

Forwards to summarizer-service’s /summarize

GET /api/notes, POST /api/notes

Forwards to notes-service

🧪 Test Target:
Unit test: route-forwarding logic (i.e., httpx client calls)

Integration test: test that forwarding works and services respond correctly
