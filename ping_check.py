import subprocess
import ipaddress
import platform



def read_file(file_path):
	list_ip = []
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			for line in file:
				ip_encontrada=line.strip()
				if not ip_encontrada:
					continue
				if check_ip(ip_encontrada):
					list_ip.append(ip_encontrada)
				else:
					print(f"🔴 Dirección IP no válida encontrada en el archivo: {ip_encontrada}")
		return list_ip
	except FileNotFoundError:
		print("El archivo no se encontró.")
		return []

def check_ip(dirrec_ip):
	
	try:
		ipaddress.ip_address(dirrec_ip)
		return True
	except ValueError:
		return False
	
		
def run_process(ips_prueba):

	parametro_ping = "-n" if platform.system().lower() == "windows" else "-c"

	for ip_unica in ips_prueba:
		print(f"Ejecutando ping para la dirección IP: {ip_unica}")
		try:
			resultado=subprocess.run (["ping", parametro_ping, "2", ip_unica],stdout=subprocess.PIPE, stderr=subprocess.PIPE,timeout=5, text=True)
		except subprocess.CalledProcessError as e:
			print(f"Error: {e.stderr.decode()}")
		except subprocess.TimeoutExpired:
			print(f"🔴 Tiempo de espera agotado para {ip_unica}")
			continue
		if resultado.returncode == 0:
				print(f"🟢 Ping exitoso para {ip_unica}")
		else:
				print(f"🔴 Ping fallido para {ip_unica}")


if __name__ == "__main__":
	result_ip=read_file("hosts.txt")
	if result_ip:	
		run_process(result_ip)
