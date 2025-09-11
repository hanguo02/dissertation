import pandas as pd, requests, io, zipfile
# Domestic D3
d3 = pd.read_excel("D3.ods", engine="odf", sheet_name="Data")
# Non-domestic bulk zip
r = requests.get("https://epc.opendatacommunities.org/api/v1/non-domestic/certificates?download=true", auth=...)
z = zipfile.ZipFile(io.BytesIO(r.content))
nd = pd.read_csv(z.open("certificates.csv"))
