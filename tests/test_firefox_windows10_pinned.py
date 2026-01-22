from furl_ai_exercise.models import ReleaseInfo, SoftwareQuery
from furl_ai_exercise.service import run_release_graph
from tests.scenario_data import (
    PINNED_WINDOWS10_DOWNLOAD_URL,
    PINNED_WINDOWS10_RELEASE_NOTES_URL,
    PINNED_WINDOWS10_VERSION,
)


def test_firefox_windows10_pinned_release(llm):
    query = SoftwareQuery(
        vendor="Mozilla",
        software="Firefox",
        os_name="Windows",
        os_version="10",
        cpu_arch="x86_64",
        version=PINNED_WINDOWS10_VERSION,
    )

    result = run_release_graph(query, llm)

    assert result == ReleaseInfo(
        release_notes_url=PINNED_WINDOWS10_RELEASE_NOTES_URL,
        download_url=PINNED_WINDOWS10_DOWNLOAD_URL,
        version=PINNED_WINDOWS10_VERSION,
    )
