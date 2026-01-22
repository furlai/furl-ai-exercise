from furl_ai_exercise.models import ReleaseInfo, SoftwareQuery
from furl_ai_exercise.service import run_release_graph


def test_firefox_windows7_esr_release(llm):
    query = SoftwareQuery(
        vendor="Mozilla",
        software="Firefox",
        os_name="Windows",
        os_version="7",
        cpu_arch="x86_64",
        version="115.0esr",
    )

    result = run_release_graph(query, llm)

    assert result == ReleaseInfo(
        release_notes_url="https://www.firefox.com/en-US/firefox/115.0esr/releasenotes/",
        download_url="https://ftp.mozilla.org/pub/firefox/releases/115.1.0esr/win64/en-US/Firefox%20Setup%20115.1.0esr.msi",
        version="115.0esr",
    )
