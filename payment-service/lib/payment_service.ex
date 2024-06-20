defmodule PaymentService do
  use Plug.Router

  plug :match
  plug :dispatch

  get "/payments" do
    send_resp(conn, 200, "Payment processed successfully!")
  end

  match _ do
    send_resp(conn, 404, "Oops, not found!")
  end
end

Plug.Adapters.Cowboy.http PaymentService, []
