from keycloak import Client

kc = Client(callback_uri="http://localhost:8001/")

at = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ5MVpVdkpBaE1KMGFMVVcwSS1aR0NMRGswd19xTGNKMXE1T2d1Si1xZEtJIn0.eyJleHAiOjE2MzEwMzM4ODIsImlhdCI6MTYzMTAzMDI4MiwiYXV0aF90aW1lIjoxNjMxMDI5NzkwLCJqdGkiOiI4MThhMDRiZi0wMzE2LTQ3YjYtOTUyNy1kYzgxZDFjNTljZGUiLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvYXV0aC9yZWFsbXMvZGVmYXVsdCIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiJmZmUwYzZmYi0yNDQ5LTRhMTItOTdhYi1lMmQ4ODhmZThlYzgiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJwb2MiLCJub25jZSI6IkxublpYOVJtdEt5S2o3aWZZNkpVbGU0V2NaRFdTZXVQIiwic2Vzc2lvbl9zdGF0ZSI6ImQ2Mjg4NTMwLWE5OWQtNDhlMS1iY2Y4LWJlNThlYjQ1MWQ0NyIsImFjciI6IjAiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLWRlZmF1bHQiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJkNjI4ODUzMC1hOTlkLTQ4ZTEtYmNmOC1iZTU4ZWI0NTFkNDciLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6ImpvaG5kb2UiLCJlbWFpbCI6ImpvaG5AZG9lLmNvbSJ9.TLyAhJEx9ddRveKpS4Vzsh0P3_9qjh2VVKERYpX7Z1YwLBYnBpXWXo4mP8DLuvUQW-zKb9DIxGBM7ZWzOa8q9Y9ZwInDPk7pEAEKOzo1MtdfVo57NqvxjWpmkS4A34bUM6igC90kQ-76jnhd98IJ66aMdxa4NjpvkNtx3lpo32tadyA52HI8qWy58Qr8O182hoECKt9BGb-qs9kN59tZvuwKepOZ1qUO6CB2_02ikWq1k5Fpf2yV3IlNfDXH3Mjo0n9r4GCbQJ2mjIa_QeZmIv6yF3-hmNoGJ3eWfpuQg4ncBfyAozXdP2Ef4ewM285o4K6XGjvTKHfB19CjsbtdvQ"

if __name__=="__main__":
    print(kc.resources)
    # res = kc.login()
    # print("Login: " + str(res))
    # res = kc.fetch_userinfo(access_token=at)
    res = kc.fetch_userinfo()
    print("User info: " + str(res))
    res = kc.payload_for_client()
    print("Client payload: " + str(res))
    res = kc.payload_for_user("johndoe", "johndoe")
    print("User payload: "+ str(res))
    res = kc.pat()
    # at = res["access_token"]
    print("PAT: " + str(res))
    # res = kc.ticket(kc.resources)
    # res = kc.ticket(access_token=at)
    # print("Permission ticket: " + str(res))
    res = kc.rpt(access_token=at)
    rpt = res["access_token"]
    print("RPT: " + str(res))
    print("RPT: " + str(kc.decode(rpt)))
    res = kc.introspect(rpt=rpt)
    print("Introspect: " + str(res))

    print("Tokens: " + str(kc.tokens))
    print("Scopes: " + str(kc.scope))
    # print("JWKS: " + str(kc.jwks))

    print(kc.resources)