type Url = {
  id: number;
  long_url: string;
  short_code: string;
  clicks: number;
};

export default function UrlList({ urls }: { urls: Url[] }) {
  if (!urls.length) return null;

  return (
    <div className="list">
      <h3>Recent Links</h3>

      {urls.map((u) => (
        <div key={u.id} className="list-item">
          <div className="list-left">
            <a
              href={`https://url-shortner-p316.onrender.com/${u.short_code}`}
              target="_blank"
            >
              /{u.short_code}
            </a>
            <span className="clicks">{u.clicks} clicks</span>
          </div>

          <div className="long-url">{u.long_url}</div>
        </div>
      ))}
    </div>
  );
}