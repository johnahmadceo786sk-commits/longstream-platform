export const connectSocket = () => {
  return new WebSocket("ws://localhost:8000/ws/updates");
};