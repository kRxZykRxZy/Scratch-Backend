import random
import secrets
import json
from flask import jsonify
from .. import db  # your db import

def create_project(app):
    @app.route('/user/<username>/projects/new', methods=['POST'])
    def new_project(username):
        # Get new project ID (max + 1)
        max_id_row = db.query("SELECT MAX(id) as max_id FROM projects")
        new_id = (max_id_row[0]['max_id'] or 0) + 1

        project_token = secrets.token_hex(32)
        project = {
            "id": new_id,
            "title": "Untitled Project",
            "description": None,
            "instructions": None,
            "visibility": None,
            "public": None,
            "comments_allowed": None,
            "is_published": None,
            "author": {
                "id": None,
                "username": username,
                "scratchteam": None,
                "history": {"joined": None},
                "profile": {
                    "id": None,
                    "images": {
                        "90x90": None,
                        "60x60": None,
                        "55x55": None,
                        "50x50": None,
                        "32x32": None
                    }
                }
            },
            "image": None,
            "images": {
                "282x218": None,
                "216x163": None,
                "200x200": None,
                "144x108": None,
                "135x102": None,
                "100x80": None
            },
            "history": {"created": None, "modified": None, "shared": None},
            "stats": {"views": None, "loves": None, "favorites": None, "remixes": None},
            "remix": {"parent": None, "root": None},
            "project_token": project_token
        }

        projectSb3_base64 = (
            "UEsDBAoAAAAIAGVpBVt8R4hu9wEAAFgDAAAMAAAAcHJvamVjdC5qc29ujVJNb9NAEP0r1nJJJeP428Y9QBVRQG3hkIiCqkqMvePUxOu1dtduQsh/"
            "ZzYfou0FbvNm3r55MztbZkAt0WhW3G1Zo+cGlsgKowZ0WQeCYnbIuWwE1UDZInG37MfP96t38e/m7tXl6u0kX59dfPVei41zIpEeewpd/37nsrbRttWWwlJJ4BX8xa2sVse4kkJgd6pUg1KEZlKbwRryLWEfH1wfbZZQrbiSfUBWORi4lEqAoYIel5QCrdF84oQrHgZJEHM/iYKa13UZhqEfo49VgjyPgciCJ7g2/8H1DuJKGjCN7GbkE9U3VoSx/zL7nRVB7u/uXabl0PFn3nvZP7OYR/AmyzMeV2VaR2WWRmEZc15jWWdxlGYvR3yEkVL1CVpHYEg4zn2fjGgQfYszakvVIAijJxP+q5Vnta3rUbb79QdWsYUNqi+Ko9r/h0HRS1akFI4NR7lQ0Oke6NuqDSuSU5ouybpismP2zdos5LxHrB6uoVsO+8vrhra13YTsGiOV3RIhomKnaZVHLNCAvUKNYrQWWOT5nm9vVBAIAi/aI1K0E7Mb+atpW5gmnu9MbpuOy0ftfF44AT06dyiRxufOOo3PnIueFnWL5VVjpkmUeVHqTK4+Lm6uXadtVuh8wGolz5zZg5ICp0GU276kOoeaLv34hO12fwBQSwMECgAAAAgAZWkFW5/xha41AgAAMAIAACQAAAA4M2E5Nzg3ZDRjYjZmM2I3NjMyYjRkZGZlYmY3NDM2Ny53YXYBMALP/VJJRkYoAgAAV0FWRWZtdCAQAAAAAQABABErAAAiVgAAAgAQAGRhdGEEAgAA1QADA70Hcg3vFVMdPCObJOIgqxZzBlXxX9pgxI2zaamSqOWxR8VB4fMC7SbRR0phfW8jcAphzkTqHSrzD8lqp/2RJY3umDm16N3iDJ06RGBwdrV5omjYRWcXSuRstXqS3oFrhnGfjsgh/OIwfV3feeR/N3GpTbYcqedPuIyWA4lpkU+u9dlcDAA8UF/vbxdpVk4KJHHyWcVno7aTeJn4smjaowmONmtXKWaiX7xG9R/I8gPK9a3Ooh+rMsTx6sAUqzkoUfFWNElOKwMELNu+uuyoDqnRvIzdvAY8LoBLFFknUl05rBMc6nHFra0pp7qzG9Cw9qUeej/IUcpRaz99H+f509aBvh+2Vb6s1bz1KhiCM/VBhEAsLwwTV/Kf1bPD9b90y5zjegJ6IIk2hj/SODokwwaS5xvOhr8IwBXPUelrCH4lIDoIQbU4liNTBi/oVs8qwurCWtEF6kkHlCLXNdA87DVKI1oJR+4b2HfLDctm1m/qsQKSGTMqeDCqKzwd9Ahk87/huNf21qzfEO/NASkTXB+oI0gfqxOvA1LzcOa639vgM+nM9iQG2xPyHEofhBrJD3wB5PI15w3hhuF66Gf0oQIsEF8aEB+MHV4WPQt0/ufyyuqW54Tp4O/5+NQCCAtKEJIR2Q43CRkCefud9pb03fXX+R//jgSXCBcKighVBGH+UEsDBAoAAAAIAGVpBVuIzhABkwAAAMoAAAAkAAAAY2QyMTUxNGQwNTMxZmRmZmIyMjIwNGUwZWM1ZWQ4NGEuc3ZnbU1LDoMgFNx7ite3B8SuNMKiSU/QE7RKhFTFwKvQ29dal01mMZlvG9cBVhOi87NCySVCcj1ZhRWCNW6wtNPVmXTxWSGTsKGCTcvTOEeFlmhphEgp8XTmPgyiKstSbMNHpMmjm5//grKua7G7qAuA9sQYXPPiA5keHm+4deFOnQUGRzf+BD454qZ/CWBMF+33S38AUEsBAhQACgAAAAgAZWkFW3xHiG73AQAAWAMAAAwAAAAAAAAAAAAAAAAAAAAAAHByb2plY3QuanNvblBLAQIUAAoAAAAIAGVpBVuf8YWuNQIAADACAAAkAAAAAAAAAAAAAAAAACECAAA4M2E5Nzg3ZDRjYjZmM2I3NjMyYjRkZGZlYmY3NDM2Ny53YXZQSwECFAAKAAAACABlaQVbiM4QAZMAAADKAAAAJAAAAAAAAAAAAAAAAACYBAAAY2QyMTUxNGQwNTMxZmRmZmIyMjIwNGUwZWM1ZWQ4NGEuc3ZnUEsFBgAAAAADAAMA3gAAAG0FAAAAAA=="
        )

        # Insert new row
        db.query(f"""
            INSERT INTO projects (id, author, projectSb3, metadata, remixes, isRemixe)
            VALUES (
                {new_id},
                '{username}',
                '{projectSb3_base64}',
                '{json.dumps(project)}',
                '{}',
                FALSE
            )
        """)

        return jsonify(project), 201
