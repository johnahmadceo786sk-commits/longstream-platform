"use client"

import { useEffect, useRef } from "react"
import Hls from "hls.js"

export default function HLSPlayer({ src }: { src: string }) {
  const videoRef = useRef<HTMLVideoElement>(null)

  useEffect(() => {
    if (!videoRef.current) return

    if (Hls.isSupported()) {
      const hls = new Hls()
      hls.loadSource(src)
      hls.attachMedia(videoRef.current)
    } else {
      videoRef.current.src = src
    }
  }, [src])

  return (
    <video
      ref={videoRef}
      controls
      style={{ width: "100%", maxWidth: 900 }}
    />
  )
}