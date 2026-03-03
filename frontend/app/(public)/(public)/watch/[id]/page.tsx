"use client";

import { useEffect, useState } from "react";
import { api } from "@/app/lib/api";
import HLSPlayer from "@/app/components/HLSPlayer";
import { useParams } from "next/navigation";

export default function WatchPage() {
  const { id } = useParams();
  const [url, setUrl] = useState("");

  useEffect(() => {
    const load = async () => {
      const res = await api.get(`/stream/${id}`);
      setUrl(`http://localhost:8000/${res.data.hls_url}`);
    };
    load();
  }, [id]);

  return (
    <div style={{ padding: 40 }}>
      <h2>Watch Video</h2>
      {url && <HLSPlayer src={url} />}
    </div>
  );
}