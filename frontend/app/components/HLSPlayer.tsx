"use client";

import { useEffect, useRef } from "react";
import Hls from "hls.js";

export default function HLSPlayer({ src }: { src: string }) {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    if (videoRef.current && Hls.isSupported()) {
      const hls = new Hls();
      hls.loadSource(src);
      hls.attachMedia(videoRef.current);
    }
  }, [src]);

  return <video ref={videoRef} controls width="800" />;
}