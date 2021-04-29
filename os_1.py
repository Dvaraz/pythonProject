import os

print(os.environ)
if 'ADSK_CLM_WPAD_PROXY_CHECK' in os.environ:
    print("yes")