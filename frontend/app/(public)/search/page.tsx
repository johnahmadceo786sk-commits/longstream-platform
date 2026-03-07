"use client"

import { useState } from "react"
import SearchBar from "@/components/SearchBar"
import VideoCard from "@/components/VideoCard"
import { searchVideos } from "@/lib/api"

export default function SearchPage() {
  const [videos, setVideos] = useState<any[]>([])

  async function handleSearch(query: string) {
    const data = await searchVideos(query)
    setVideos(data)
  }

  return (
    <div>
      <h2>Search</h2>

      <SearchBar onSearch={handleSearch} />

      <div style={{ marginTop: 20 }}>
        {videos.map((v) => (
          <VideoCard key={v.id} video={v} />
        ))}
      </div>
    </div>
  )
}