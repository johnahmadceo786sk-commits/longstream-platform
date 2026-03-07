"use client"

import { useParams } from "next/navigation"
import HLSPlayer from "@/components/HLSPlayer"

export default function WatchPage() {
  const params = useParams()

  const videoId = params.id as string

  const src = `http://localhost:8000/stream/${videoId}`

  return (
    <div>
      <h2>Watch Video</h2>

      <HLSPlayer src={src} />
    </div>
  )
}