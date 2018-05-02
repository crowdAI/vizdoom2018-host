import gitlab
from crowdai_api import API as CROWDAI_API
import os

def _authenticate_gl():
    GITLAB_URL=os.environ["CROWDAI_GITLAB_URL"]
    GITLAB_AUTH_TOKEN=os.environ["CROWDAI_GITLAB_AUTH_TOKEN"]
    gl = gitlab.Gitlab(GITLAB_URL, private_token=GITLAB_AUTH_TOKEN, ssl_verify=False)

    return gl

def _authenticate_crowdai():
    CROWDAI_AUTH_TOKEN=os.environ["CROWDAI_AUTH_TOKEN"]
    crowdai_api = CROWDAI_API(CROWDAI_AUTH_TOKEN)
    return crowdai_api


def update_issue_state(states):
    if "CROWDAI_EVALUATION" not in os.environ.keys():
        return

    print("Updating states to : ", states)
    gl = _authenticate_gl()

    PROJECT_ID=os.environ["GITLAB_PROJECT_ID"]
    ISSUE_ID=os.environ["GITLAN_ISSUE_ID"]

    project = gl.projects.get(int(PROJECT_ID))
    issue=gl.projects.issues.get(int(ISSUE_ID))
    issue.labels=states
    issue.save()

def update_submission_score(username, score):
    if "CROWDAI_EVALUATION" not in os.environ.keys():
        return

    SUBMISSION_ID = int(os.environ["CROWDAI_SUBMISSION_ID"])
    CHALLENGE_ID = os.environ["CROWDAI_CHALLENGE_ID"]

    crowdai_api = _authenticate_crowdai()
    submission = crowdai_api.get_submission(CHALLENGE_ID, SUBMISSION_ID)
    submission.score = score
    submission.grading_status = "graded"
    submission.update()

def mark_submission_failed(username):
    if "CROWDAI_EVALUATION" not in os.environ.keys():
        return

    SUBMISSION_ID = int(os.environ["CROWDAI_SUBMISSION_ID"])
    CHALLENGE_ID = os.environ["CROWDAI_CHALLENGE_ID"]

    crowdai_api = _authenticate_crowdai()
    submission = crowdai_api.get_submission(CHALLENGE_ID, SUBMISSION_ID)
    submission.score = score
    submission.grading_status = "graded"
    submission.update()
