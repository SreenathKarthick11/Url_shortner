import { useState } from "react";
import UrlInput from "../components/UrlInput";
import ResultBox from "../components/ResultBox";
import { shortenUrl } from "../services/api";
import { Link } from "react-router-dom";

export default function Home() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleShorten = async () => {
    if (!url) return setError("Enter URL");

    setLoading(true);
    setError("");

    try {
      const data = await shortenUrl(url);
      setShortUrl(data.short_url);
    } catch {
      setError("Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1 className="title">URL Shortener</h1>

      <UrlInput
        url={url}
        setUrl={setUrl}
        onSubmit={handleShorten}
        loading={loading}
      />

      {error && <p className="error">{error}</p>}

      <ResultBox shortUrl={shortUrl} />

      <Link to="/dashboard" className="nav-link">
        View Dashboard →
      </Link>
    </div>
  );
}