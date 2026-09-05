#### Data preprocessing
- Data loader:
	Requiere de importar las constantes de configuración:
	1. ALL_MONTAGES
	2. CORPUS_PATHS
	3. BASE_PATH
	
	Contiene funciones para:
	1. ```get_session_data(***kwargs)``` 
		Extraer los datos por sessión, paciente y montaje, permite hacer delimitaciones de los datos para pruebas.
	2. ```load_raw_edf(***kwargs)``` 
	3. ```load_annotations(***kwargs)``` 
	4. ```build_annotations_index(***kwargs)``` 
		Crea un dataframe con la metadata de los pacientes (paciente, sesión, sección y montaje)
	5. 