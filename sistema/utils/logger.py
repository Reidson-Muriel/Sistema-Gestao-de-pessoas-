import logging, os

# ve para que a pasta logs existe
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
  filename="logs/app.log",
  level=logging.ERROR,
  format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)