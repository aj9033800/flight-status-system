import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FlightStatus = () => {
    const [status, setStatus] = useState('Loading...');

    useEffect(() => {
        const fetchStatus = async () => {
            const response = await axios.get('/api/flight/status');
            setStatus(response.data.status);
        };
        fetchStatus();
    }, []);

    return (
        <div>
            <h1>Flight Status</h1>
            <p>{status}</p>
        </div>
    );
};

export default FlightStatus;
