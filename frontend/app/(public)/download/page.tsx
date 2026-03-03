"use client";

import { useState } from "react";
import { api } from "@/app/lib/api";

export default function DownloadPage() {
  const [videoId, setVideoId] = useState("");

  const handleDownload = async () => {
    const res = await api.get(`/download/${videoId}`);
    window.location.href = `http://localhost:8000/${res.data.download_file}`;
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>Download Video</h2>
      <input
        placeholder="Video ID"
        value={videoId}
        onChange={(e) => setVideoId(e.target.value)}
      />
      <button onClick={handleDownload}>Download</button>
    </div>
  );
}