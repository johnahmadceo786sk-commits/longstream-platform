"use client"

import { useEffect, useState } from "react"

type Analytics = {
  totalViews: number
  totalVideos: number
  bandwidthUsed: number
}

export default function AnalyticsPage() {

  const [data, setData] = useState<Analytics | null>(null)

  useEffect(() => {
    const loadAnalytics = async () => {
      try {
        const res = await fetch("/api/analytics")

        if (res.ok) {
          const json = await res.json()
          setData(json)
        }
      } catch (err) {
        console.error(err)
      }
    }

    loadAnalytics()
  }, [])

  if (!data) {
    return (
      <div className="p-10">
        Loading analytics...
      </div>
    )
  }

  return (
    <div className="p-10">

      <h1 className="text-3xl font-bold mb-8">
        Analytics
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <div className="bg-white shadow p-6 rounded-xl">
          <h2 className="text-lg font-semibold">Total Views</h2>
          <p className="text-3xl font-bold mt-2">
            {data.totalViews}
          </p>
        </div>

        <div className="bg-white shadow p-6 rounded-xl">
          <h2 className="text-lg font-semibold">Videos Uploaded</h2>
          <p className="text-3xl font-bold mt-2">
            {data.totalVideos}
          </p>
        </div>

        <div className="bg-white shadow p-6 rounded-xl">
          <h2 className="text-lg font-semibold">Bandwidth Used</h2>
          <p className="text-3xl font-bold mt-2">
            {data.bandwidthUsed} GB
          </p>
        </div>

      </div>

    </div>
  )
}