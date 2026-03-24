import { useEffect, useState } from "react";
import UrlList from "../components/UrlList";
import { getUrls } from "../services/api";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const [urls, setUrls] = useState([]);

  const fetchUrls = async () => {
    try {
      const data = await getUrls();
      setUrls(data);
    } catch {
      console.log("error fetching urls");
    }
  };

  useEffect(() => {
    fetchUrls();
  }, []);

  return (
    <div className="container">
      <h1 className="title">Dashboard</h1>

      <UrlList urls={urls} />

      <Link to="/" className="nav-link">
        ← Back
      </Link>
    </div>
  );
}