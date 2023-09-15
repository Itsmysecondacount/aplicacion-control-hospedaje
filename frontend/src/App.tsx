import { useState } from 'react'
import './App.css'
import { useEffect } from 'react';
import axios from 'axios';

function App() {

	const [data, setData] = useState<Cliente[]>([]);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await axios.get<Cliente[]>(
					'http://backend:8010/clientes/?skip=0&limit=10',
					{
						headers: {
							accept: 'application/json',
						},
					},
				);
				setData(response.data);
			} catch (error) {
				console.error('Hubo un error al obtener los datos:', error);
			}
		};

		fetchData();
	}, []);

	return (
		<div>
			<h1>Clientes</h1>
			{data.map((cliente, index) => (
				<div key={index}>
					<p>ID: {cliente.ClienteID}</p>
					<p>Nombre: {cliente.Nombre}</p>
					<p>Apellidos: {cliente.Apellido}</p>
					{/* ... otros campos */}
				</div>
			))}
		</div>
	);
}

export default App;
