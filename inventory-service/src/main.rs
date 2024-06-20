use actix_web::{web, App, HttpResponse, HttpServer, Responder};

async fn check_inventory() -> impl Responder {
    HttpResponse::Ok().body("Inventory check successful")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/inventory", web::get().to(check_inventory))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
