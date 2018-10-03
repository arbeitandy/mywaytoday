
# === Day2 Ideas covered ===

"""
1. local jupyter
2. gcp setup and init
3. deploy jupyter
4. add password to jupyter
5. monitor logs on gcp
6. monitor cost on gcp
7. scale instances on gcp

"""

# === Day1 Section 1 ===

"""
Dockerfile for running jupiter 
"""


# === Day1 Section 7 ===

"""
use gcp datalab directly (not free)
https://cloud.google.com/datalab/docs/quickstart
"""
gcloud components update
gcloud components install datalab
datalab create lets_data
open http://localhost:8081
datalab delete --delete-disk instance-name
"""
made by [Pycco][pycco]

[Home][home]

[pycco]: https://pycco-docs.github.io/pycco/
[home]: http://d.fogtown.us/
"""
