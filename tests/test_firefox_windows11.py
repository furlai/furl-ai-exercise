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

    assert isinstance(result, ReleaseInfo)

    # Release notes should point to Mozilla/Firefox notes page
    assert "mozilla.org" in result.release_notes_url or "firefox.com" in result.release_notes_url
    assert "firefox" in result.release_notes_url.lower()

    # Download URL should be Mozilla's official download service
    assert "mozilla.org" in result.download_url
    assert "firefox" in result.download_url.lower() or "product=firefox" in result.download_url.lower()

    # Version should be present
    assert result.version
