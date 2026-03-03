"use client";

import { useEffect, useState } from "react";
import { api } from "@/app/lib/api";
import VideoCard from "@/app/components/VideoCard";
import SearchBar from "@/app/components/SearchBar";

export default function SearchPage() {
  const [videos, setVideos] = useState([]);

  const fetchVideos = async (query?: string) => {
    const url = query ? `/search?query=${query}` : `/videos`;
    const res = await api.get(url);
    setVideos(res.data);
  };

  useEffect(() => {
    fetchVideos();
  }, []);

  return (
    <div style={{ padding: 30 }}>
      <h2>Search Videos</h2>
      <SearchBar onSearch={fetchVideos} />
      {videos.map((video: any) => (
        <VideoCard key={video.id} video={video} />
      ))}
    </div>
  );
}