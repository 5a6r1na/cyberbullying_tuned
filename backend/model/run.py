import json
import sys
from model import stage1_output, generate_peer_rationale

# Read arguments
comment = sys.argv[1]
age = int(sys.argv[2])
ethnicity = sys.argv[3]

# Stage 1 classification
label, resources, message = stage1_output(comment)

if label == "not_cyberbullying":
    print(json.dumps({
        "flag": -1,
        "label": label,
        "response": None
    }))
    sys.exit(0)

# If bullying → generate rationale
peer_msg = generate_peer_rationale(comment, label, age)

print(json.dumps({
    "flag": 1,
    "label": label,
    "resources": resources,
    "response": message + "\n\n" + peer_msg
}))
