"use client";

import { useState } from "react";
import { api } from "@/app/lib/api";
import { useRouter } from "next/navigation";

export default function Login() {
  const [username, setUsername] = useState("john");
  const [password, setPassword] = useState("CEOjohn$$");
  const router = useRouter();

  const handleLogin = async () => {
    const res = await api.post("/auth/login", { username, password });
    localStorage.setItem("token", res.data.access_token);
    router.push("/dashboard");
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>Host Login</h2>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}