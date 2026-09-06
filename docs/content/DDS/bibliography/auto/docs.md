# Bibliografía auto — DDS

## securing-high-concurrency-ticket-sales-microservice

- **Título:** Securing High-Concurrency Ticket Sales: A Framework Based on Microservice
- **Autores:** Zhiyong Zhang, Xiaoyan Zhang, Xiaoqi Li
- **Keywords:** microservices; high concurrency; overselling; Redis; inventory tokens; Spring Cloud
- **Razón:** Ancla el invariante **0 oversell** bajo concurrencia (deducción atómica de cupo/token antes de persistir), transferible al mecanismo `ReservarStockAlCrearPedido` del PoC (citar el patrón, no el dominio de tickets ni Redis como obligatorio).
- **Cita:** Zhang, Z., Zhang, X., & Li, X. (2025). Securing high-concurrency ticket sales: A framework based on microservice. *arXiv*. https://doi.org/10.48550/arXiv.2512.24941
- **DOI / URL:** https://arxiv.org/abs/2512.24941 · https://doi.org/10.48550/arXiv.2512.24941
- **PDF:** `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf`
- **MD:** `bibliography/docs/securing-high-concurrency-ticket-sales-microservice.md`
- **Estado:** `ok`

## distributed-transactions-microservice-architecture

- **Título:** Distributed Transactions in Microservice Architecture: Informed Decision-Making Strategies
- **Autores:** Artem Bashtovyi, Andrii Fechan
- **Keywords:** distributed transactions; microservices; decisions; guidance; consistency; distributed systems
- **Razón:** Fundamenta la decisión de consistencia pedido↔inventario en el camino a microservicios (p. ej. transacción local en el PoC vs 2PC/saga prematuros), alineada al ADR/objetivo arquitectónico del profile.
- **Cita:** Bashtovyi, A., & Fechan, A. (2024). Distributed transactions in microservice architecture: Informed decision-making strategies. *Information Systems and Networks*, (15), 449–459. https://doi.org/10.23939/sisn2024.15.449
- **DOI / URL:** https://doi.org/10.23939/sisn2024.15.449
- **PDF:** `bibliography/auto/pdfs/distributed-transactions-microservice-architecture.pdf`
- **MD:** `bibliography/docs/distributed-transactions-microservice-architecture.md`
- **Estado:** `ok`
