export default function NotificationToast({ message }: { message: string }) {
  return (
    <div
      style={{
        position: "fixed",
        bottom: 20,
        right: 20,
        background: "#1e293b",
        padding: 14,
        borderRadius: 8
      }}
    >
      {message}
    </div>
  )
}