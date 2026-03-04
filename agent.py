"""
Agent for communicating with the Vector DB Storage API.
Provides methods to fetch, search, and post information to/from the database.
"""
import httpx
from typing import List, Dict, Optional, Any
import json


class VectorDBAgent:
    """Agent for interacting with the Vector DB Storage API."""
    
    def __init__(self, base_url: str = "http://localhost:8000", timeout: float = 30.0):
        """
        Initialize the agent.
        
        Args:
            base_url: Base URL of the API server
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.client = httpx.Client(timeout=timeout)
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close the client."""
        self.close()
    
    def close(self):
        """Close the HTTP client."""
        self.client.close()
    
    # ===== Health & Statistics =====
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check if the API server is running.
        
        Returns:
            Health status information
        """
        response = self.client.get(f"{self.base_url}/")
        response.raise_for_status()
        return response.json()
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get collection statistics.
        
        Returns:
            Statistics including total document count
        """
        response = self.client.get(f"{self.base_url}/stats")
        response.raise_for_status()
        return response.json()
    
