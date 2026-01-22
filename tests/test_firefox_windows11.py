from furl_ai_exercise.models import ReleaseInfo, SoftwareQuery
from furl_ai_exercise.service import run_release_graph


def test_firefox_windows11_latest_release(llm):
    query = SoftwareQuery(
        vendor="Mozilla",
        software="Firefox",
        os_name="Windows",
        os_version="11",
        cpu_arch="x86_64",
    )

    result = run_release_graph(query, llm)

    assert result == ReleaseInfo(
        release_notes_url="https://www.mozilla.org/en-US/firefox/notes/latest/",
        download_url="https://download.mozilla.org/?product=firefox-latest-ssl&os=win&lang=en-US",
        version="latest",
    )
