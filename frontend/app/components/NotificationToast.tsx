"use client";

import { useEffect } from "react";
import { connectSocket } from "@/app/lib/websocket";

export default function NotificationToast() {
  useEffect(() => {
    const socket = connectSocket();

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      alert(`New Video Uploaded: ${data.title}`);
    };
  }, []);

  return null;
}