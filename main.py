from flask import Flask, jsonify
import logging
from datetime import datetime
from src.q1_time import q1_time
from src.q1_memory import q1_memory
from src.q2_time import q2_time
from src.q2_memory import q2_memory
from src.q3_time import q3_time
from src.q3_memory import q3_memory

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# File path for the JSON data
file_path = "/app/farmers-protest-tweets-2021-2-4.json"

@app.route('/run', methods=['GET'])
def process_files():
    try:
        # Log the start of the process
        logger.info("Starting data processing...")

        # Execute and log each function
        logger.info("Running q1_time...")
        q1_time_result = q1_time(file_path)
        logger.info(f"q1_time result: {q1_time_result}")

        logger.info("Running q1_memory...")
        q1_memory_result = q1_memory(file_path)
        logger.info(f"q1_memory result: {q1_memory_result}")

        logger.info("Running q2_time...")
        q2_time_result = q2_time(file_path)
        logger.info(f"q2_time result: {q2_time_result}")

        logger.info("Running q2_memory...")
        q2_memory_result = q2_memory(file_path)
        logger.info(f"q2_memory result: {q2_memory_result}")

        logger.info("Running q3_time...")
        q3_time_result = q3_time(file_path)
        logger.info(f"q3_time result: {q3_time_result}")

        logger.info("Running q3_memory...")
        q3_memory_result = q3_memory(file_path)
        logger.info(f"q3_memory result: {q3_memory_result}")

        # Log the end of the process
        logger.info("Data processing completed.")

        return jsonify({
            'q1_time_result': q1_time_result,
            'q1_memory_result': q1_memory_result,
            'q2_time_result': q2_time_result,
            'q2_memory_result': q2_memory_result,
            'q3_time_result': q3_time_result,
            'q3_memory_result': q3_memory_result
        }), 200
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'message': f'Error: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
