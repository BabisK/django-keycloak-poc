import json
from keycloak import KeycloakOpenID

keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                    client_id="perm",
                    realm_name="default",
                    client_secret_key="a744f7b7-a7e2-4a35-96c2-520cf930a031",
                    verify=True)

def j(jsons: str):
    return json.dumps(jsons, indent=2)

if __name__=="__main__":
    config_well_know = keycloak_openid.well_know()
    print("Well known: " + j(config_well_know))

    token = keycloak_openid.token("johndoe", "johndoe")
    # print("Token: " + j(token))
    intr = keycloak_openid.introspect(token=token["access_token"])
    # print("Intr: " + j(intr))

    userinfo = keycloak_openid.userinfo(token['access_token'])
    # print("User info: " + j(userinfo))

    # keycloak_openid.load_authorization_config()
    # policies = keycloak_openid.get_permissions(token["access_token"])
    # print(policies)
    # print("RPT: " + j(rpt))