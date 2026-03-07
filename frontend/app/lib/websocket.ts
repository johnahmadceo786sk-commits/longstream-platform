export function connectUpdates(onMessage: (msg: string) => void) {
  const ws = new WebSocket("ws://localhost:8000/ws")

  ws.onmessage = (event) => {
    onMessage(event.data)
  }

  return ws
}