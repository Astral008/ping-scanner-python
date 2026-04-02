import subprocess
import ipaddress


list_ip = []
# funciones
def read_file(file_path):
	
	try:
		with open(file_path, 'r') as file:
			for line in file:
				ip_encontrada=line.strip()
				if check_ip(ip_encontrada):
					list_ip.append(ip_encontrada)
				else:
					print(f"Dirección IP no válida encontrada en el archivo: {ip_encontrada}")
		return list_ip
	except FileNotFoundError:
		print("El archivo no se encontró.")

def check_ip(dirrec_ip):
	
	try:
		ipaddress.ip_address(dirrec_ip)
		return True
	except ValueError:
		return False
	
		
def run_process(ips_prueba):

	for ip_unica in ips_prueba:
		print(f"Ejecutando ping para la dirección IP: {ip_unica}")
		try:
			resultado=subprocess.run (["ping","-c","2" ,ip_unica],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			print (resultado.stdout)
		except subprocess.CalledProcessError as e:
			print(f"Error: {e.stderr.decode()}")

	

#PROGRAMA 


result_ip=read_file("hosts.txt")
run_process(result_ip)
